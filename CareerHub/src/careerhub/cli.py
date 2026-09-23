from __future__ import annotations

import argparse
import json
from pathlib import Path

from .application import fallback_application, run_ai_application, write_application_docx, write_hrdm_docx
from .dashboard import render_applications, render_control_room, render_job_vault, render_visual, save_public_jobs
from .hrdm import build_packet, fallback_hrdm, packet_prompt, run_ai_hrdm
from .matching import load_yaml as load_match_yaml, rank_jobs
from .sources import fetch_public_job, load_yaml as load_source_yaml, source_lane
from .state import choose_case, load_cases, merge_job_vault, update_case, update_priority


def root_from_here() -> Path:
    return Path(__file__).resolve().parents[3]


def load_profile(root: Path) -> dict:
    import yaml
    base = yaml.safe_load((root / "CareerHub/profile/candidate.yaml").read_text(encoding="utf-8"))
    local = root / "CareerHub/private/profile.local.yaml"
    if local.exists():
        override = yaml.safe_load(local.read_text(encoding="utf-8")) or {}
        for key, value in override.items():
            base[key] = value
    return base


def cmd_scan(args):
    root = root_from_here()
    profile = load_profile(root)
    search_cfg = load_match_yaml(root / "CareerHub/config/search_profiles.yaml")
    source_cfg = load_source_yaml(root / "CareerHub/config/sources.yaml")
    lanes = search_cfg["lanes"]
    lane_names = list(lanes) if args.lane == "all" else [args.lane]

    all_jobs = []
    for lane_name in lane_names:
        lane_cfg = lanes[lane_name]
        sourced = source_lane(lane_cfg["queries"], search_cfg["defaults"], source_cfg)
        ranked = rank_jobs(sourced, lane_name, lane_cfg, profile, search_cfg["defaults"])
        all_jobs.extend(ranked)

    best = {}
    for job in all_jobs:
        key = job.url or job.id
        if key not in best or job.triage_score > best[key].triage_score:
            best[key] = job

    ranked = sorted(best.values(), key=lambda j: -j.triage_score)[:args.limit]
    save_public_jobs(root / "CareerHub/data/latest_jobs.json", ranked)

    vault_path = root / "CareerHub/data/job_vault.json"
    cases_path = root / "CareerHub/data/applications.json"
    vault = merge_job_vault(vault_path, ranked)
    cases = load_cases(cases_path)

    render_visual(root / "CareerHub/visuals/careerhub-journey.svg", ranked, cases, vault)
    render_job_vault(root / "CareerHub/JOB_VAULT.md", vault, cases)
    render_applications(root / "CareerHub/APPLICATIONS.md", cases)
    render_control_room(root / "CareerHub/CONTROL_ROOM.md", ranked, args.lane, cases, vault)

    print(json.dumps({
        "jobs": len(ranked),
        "jobs_ever_seen": vault.get("total_jobs_ever_seen"),
        "lane": args.lane,
        "top_score": ranked[0].triage_score if ranked else None,
    }, indent=2))


def cmd_drill(args):
    root = root_from_here()
    profile = load_profile(root)
    outdir = Path(args.out)
    if not outdir.is_absolute():
        outdir = root / outdir
    outdir.mkdir(parents=True, exist_ok=True)

    supplied_text = args.text or ""
    if args.text_file:
        supplied_text = Path(args.text_file).read_text(encoding="utf-8")
    job = fetch_public_job(args.url, supplied_text=supplied_text)
    if args.title and not job.title:
        job.title = args.title
    if args.company and not job.company:
        job.company = args.company
    if args.deadline and not job.deadline:
        job.deadline = args.deadline
    job.lane = args.lane
    packet = build_packet(job, profile, args.lane)
    (outdir / "job.json").write_text(json.dumps(job.full_dict(), ensure_ascii=False, indent=2), encoding="utf-8")
    (outdir / "HRDM_input_packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2), encoding="utf-8")
    (outdir / "HRDM_prompt.md").write_text(packet_prompt(packet), encoding="utf-8")

    schema_path = root / "CareerHub/hrdm/hrdm_result.schema.json"
    hrdm = run_ai_hrdm(packet, schema_path) or fallback_hrdm(packet)
    (outdir / "HRDM_result.json").write_text(json.dumps(hrdm, ensure_ascii=False, indent=2), encoding="utf-8")

    app = run_ai_application(job.full_dict(), profile, hrdm, args.lane) or fallback_application(job.full_dict(), profile, hrdm)
    (outdir / "application_package.json").write_text(json.dumps(app, ensure_ascii=False, indent=2), encoding="utf-8")

    app_doc = write_application_docx(outdir, job.full_dict(), profile, app)
    hrdm_doc = write_hrdm_docx(outdir, hrdm)
    ai_used = hrdm.get("ai_status") != "not_run"

    print(json.dumps({
        "process_id": packet["process_id"],
        "application_docx": str(app_doc),
        "hrdm_docx": str(hrdm_doc),
        "ai_used": ai_used,
    }, indent=2))




def _load_latest_jobs(root: Path):
    payload = json.loads((root / "CareerHub/data/latest_jobs.json").read_text(encoding="utf-8"))
    from .models import Job
    return [Job.from_dict(j) for j in payload.get("jobs", [])]


def _render_all(root: Path):
    jobs = _load_latest_jobs(root)
    cases = load_cases(root / "CareerHub/data/applications.json")
    vault_path = root / "CareerHub/data/job_vault.json"
    if vault_path.exists():
        vault = json.loads(vault_path.read_text(encoding="utf-8"))
    else:
        vault = merge_job_vault(vault_path, jobs)
    render_visual(root / "CareerHub/visuals/careerhub-journey.svg", jobs, cases, vault)
    render_job_vault(root / "CareerHub/JOB_VAULT.md", vault, cases)
    render_applications(root / "CareerHub/APPLICATIONS.md", cases)
    render_control_room(root / "CareerHub/CONTROL_ROOM.md", jobs, "all", cases, vault)


def cmd_track(args):
    root = root_from_here()
    cases_path = root / "CareerHub/data/applications.json"

    if args.action == "choose":
        from .models import Job
        data = json.loads(Path(args.job_json).read_text(encoding="utf-8"))
        job = Job.from_dict(data)
        case = choose_case(
            cases_path,
            job,
            issue_number=args.issue_number,
            issue_url=args.issue_url,
            priority=args.priority,
        )
    elif args.action == "status":
        case = update_case(
            cases_path,
            issue_number=args.issue_number,
            status=args.status,
            event_date=args.date or "",
            next_action=args.next_action or "",
            next_action_date=args.next_action_date or "",
        )
    elif args.action == "priority":
        case = update_priority(cases_path, args.issue_number, args.priority)
    else:
        raise SystemExit(f"Unsupported tracking action: {args.action}")

    _render_all(root)
    print(json.dumps(case, ensure_ascii=False, indent=2))


def cmd_render(args):
    _render_all(root_from_here())
    print("CareerHub surfaces rendered.")


def build_parser():
    parser = argparse.ArgumentParser(prog="careerhub")
    sub = parser.add_subparsers(dest="command", required=True)

    scan = sub.add_parser("scan", help="Source and rank job leads")
    scan.add_argument("--lane", choices=["core", "adjacent", "bridge", "all"], default="all")
    scan.add_argument("--limit", type=int, default=80)
    scan.set_defaults(func=cmd_scan)

    drill = sub.add_parser("drill", help="Run HRDM/application workflow for one job")
    drill.add_argument("--url", required=True)
    drill.add_argument("--text", default="")
    drill.add_argument("--text-file", default="")
    drill.add_argument("--title", default="")
    drill.add_argument("--company", default="")
    drill.add_argument("--deadline", default="")
    drill.add_argument("--lane", choices=["core", "adjacent", "bridge"], default="core")
    drill.add_argument("--out", default="CareerHub/output")
    drill.set_defaults(func=cmd_drill)

    track = sub.add_parser("track", help="Create or update a CareerHub application case")
    track.add_argument("--action", choices=["choose", "status", "priority"], required=True)
    track.add_argument("--job-json", default="")
    track.add_argument("--issue-number", type=int, required=True)
    track.add_argument("--issue-url", default="")
    track.add_argument("--priority", type=int, default=3)
    track.add_argument("--status", default="")
    track.add_argument("--date", default="")
    track.add_argument("--next-action", default="")
    track.add_argument("--next-action-date", default="")
    track.set_defaults(func=cmd_track)

    render = sub.add_parser("render", help="Regenerate CareerHub control surfaces")
    render.set_defaults(func=cmd_render)

    return parser


def main():
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
