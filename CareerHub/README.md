# CareerHub

**CareerHub is meant to feel like a small job-search service, not a software project.**

## Use it

### 1. Open the control room
**[Open CareerHub →](CONTROL_ROOM.md)**

Current jobs are refreshed automatically on weekdays.

### 2. Choose a job
Either pick one from the CareerHub board or use:

**[Analyze any job →](https://github.com/Hybrismannen/wpb/issues/new?template=careerhub-analyze-job.yml)**

### 3. Download the finished pack
CareerHub runs the full HRDM-R process in the background and posts a link when the pack is ready.

The pack contains:
- editable application Word document
- editable HRDM brief Word document
- candidate-positioning / claims check
- structured analysis for interview preparation

Then edit the Word draft and send the application.

## What CareerHub searches for

CareerHub keeps three purposes separate:

- **Career-track** — journalism, writing, editorial, communications, press, research, culture/NGO.
- **Adjacent** — transferable content, coordination, research support, communications and project work.
- **Extra-income / flexible** — part-time, temporary and lower-barrier work where reliable income may matter more than career progression.

## What it does automatically

**Profile → job sourcing → shortlist → HRDM-R → employer/role research → candidate positioning → application draft → DOCX**

The fast shortlist is only a sourcing heuristic. A selected role receives the full HRDM-R analysis.

## What Weronika needs to know

She does **not** need to:
- edit code
- understand GitHub Actions
- understand JSON/YAML
- run HRDM manually
- maintain source APIs
- write the first application draft from scratch

She mainly needs to:
1. choose jobs,
2. click **Analyze**,
3. review the resulting Word document.

## Profile status

The current profile is grounded in the verified WPB archive. Current practical details still need Weronika's confirmation.

**[Review the human-readable profile →](profile/PROFILE_REVIEW.md)**

## Privacy

This is a public repository. Private contact details, unpublished CVs and final application documents are not committed.

Application packs are generated as temporary workflow artifacts.

See [PRIVACY.md](PRIVACY.md).

---

<details>
<summary><strong>Technical architecture</strong></summary>

CareerHub includes:
- public/API job-source adapters
- core / adjacent / bridge search profiles
- deterministic sourcing triage
- HRDM-R v6.3 structured analysis
- optional employer/role web research
- evidence-bounded application drafting
- DOCX generation
- automatic weekday job refresh
- issue-driven one-job analysis
- validation and offline DOCX smoke tests

Start with [docs/WORKFLOW.md](docs/WORKFLOW.md) if you are maintaining the system.

</details>
