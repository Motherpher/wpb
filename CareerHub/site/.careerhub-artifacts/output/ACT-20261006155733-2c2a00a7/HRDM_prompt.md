You are performing a full CareerHub HRDM-R v6.3 analysis.

Canonical Reverse sequence:
1 Ad/Text Intake
2 Signal Extraction
3 Key Words & Concepts
4 Hidden Need Reconstruction
5 Field Logic Reconstruction
6 FunctionCore Estimation
6A DoD Diagnostic
7 Likely Assessment Zones
8 Candidate Positioning Map
9 HCC Reverse Commentary

Candidate evidence rule:
- Only verified career evidence in the packet may be used as candidate facts or proof points.
- Never use private-life information, model memory, conversational impressions or search-only wishes as candidate evidence.
- Unknown means unknown.

HCC-Lite:
Review structural honesty, burden clarity, dignity/fairness, vulnerability sensitivity, non-deceptive framing and trace/accountability.

Field Logic Reconstruction:
- Use the stable field_logic contract to identify dominant logics, tensions, coordination requirements, the decision environment, implications for the role and a concise synthesis.
- Do not use field_logic as a generic free-form dumping ground.

Hybridianesque (Hy-Filter):
- Evaluate it on every run, but it is not globally active.
- Recommend/activate only when at least three of these four criteria are genuinely evidenced, with explicit evidence for each met criterion:
  1) more than one logic genuinely in play,
  2) structural asymmetry is relevant,
  3) translation/mediation does constitutive work,
  4) process materializes into usable outputs.
- Do not activate merely because a role is senior, broad, multidisciplinary or rhetorically complex.
- If relevant, perform the full enclosed interpretation: participating logics, asymmetries, translation relations, process-to-output movement, overload/misframing, failure modes and remaining risk.
- Scan only these canonical failure modes: decorative_complexity_language, prestige_coded_overload, many_hats_drift, undefined_outputs, undefined_counterparties, false_depth_through_blur.
- Never glamorize overload, invent complexity, aestheticize incoherence or reward vagueness.
- In the schema-compatible `user_decision` field return null in Auto mode. Use status `active` when you recommend activation and `not_recommended` when you do not.
- Normal mode is Auto. You own the relevance judgement; do not ask the user whether to activate the filter.

Trace discipline:
- Preserve the supplied run_id, run sequence and trace identity.
- Do not invent a new Process-ID.
- The CareerHub runtime, not the model, finalizes the Process-ID state token after successful semantic execution.
- The runtime is authoritative for the exact job object and trace map; model placeholders for those runtime-owned objects will be replaced after generation.

Return only JSON conforming to the supplied schema.

PACKET:
{
  "process_id": "HRDM-R-20261006-0001-S09-A-R01-OPEN",
  "mode": "HRDM-R-v6.3",
  "lane": "core",
  "job": {
    "source": "manual",
    "title": "WP39 End-to-End Test Role",
    "company": "CareerHub Test Harness",
    "location": "",
    "workplace_address": "",
    "latitude": null,
    "longitude": null,
    "employment_type": "",
    "work_mode": "",
    "published": "",
    "deadline": "",
    "url": "https://careerhub.local/wp39-e2e-test-6",
    "salary": "",
    "description": "This is a synthetic end-to-end verification role for CareerHub WP39. The role coordinates research, editorial production, stakeholder communication, structured analysis, evidence synthesis and delivery across multiple organisational logics. It requires translating complex qualitative material into clear public-facing outputs, managing competing institutional expectations, maintaining traceability of evidence, and producing actionable recommendations. This text exists only to verify the governed HRDM-R execution path, automatic Hybridianesque relevance evaluation, semantic analysis, durable artifact persistence and result retrieval.",
    "provider_id": "",
    "lane": "core",
    "matched_query": "",
    "triage_score": 0.0,
    "triage_reasons": [],
    "review_flags": [],
    "provider_meta": {},
    "id": "20641ef17f2f8f17"
  },
  "candidate_evidence": {
    "identity": {
      "name": "Weronika Pérez Borjas"
    },
    "career_sources": [
      {
        "id": "wpb-corpus-verified",
        "source_type": "verified_project_record",
        "reference": "../../data/corpus.json",
        "verification_status": "verified",
        "verified_at": "2026-09-24",
        "notes": "Repository corpus contains 38 recovered works; 31 are marked status=verified. Use only entries marked verified."
      },
      {
        "id": "wpb-credits-verified",
        "source_type": "verified_project_record",
        "reference": "../../data/credits.json",
        "verification_status": "verified",
        "verified_at": "2026-09-24",
        "notes": "Use only records whose dashboard.verification_status is context-verified; unresolved records are excluded."
      }
    ],
    "evidence": [
      {
        "id": "ev-wpb-001",
        "claim": "The verified repository corpus contains 31 published or reported works in Polish and English.",
        "status": "verified",
        "source_ids": [
          "wpb-corpus-verified"
        ],
        "external_use": true
      },
      {
        "id": "ev-wpb-002",
        "claim": "Verified work spans academic and cultural analysis, interviews, cultural journalism, social reporting and long-form reportage.",
        "status": "verified",
        "source_ids": [
          "wpb-corpus-verified"
        ],
        "external_use": true
      },
      {
        "id": "ev-wpb-003",
        "claim": "Verified publication outlets include Kultura Współczesna, Fashion, Style & Popular Culture, The Forumist, Totally Stockholm, VICE/VICE Polska, Duży Format/Gazeta Wyborcza, Newsweek Polska and Onet Wiadomości.",
        "status": "verified",
        "source_ids": [
          "wpb-corpus-verified"
        ],
        "external_use": true
      },
      {
        "id": "ev-wpb-004",
        "claim": "The verified corpus includes long-form reportage for Duży Format/Gazeta Wyborcza, Newsweek Polska and Onet Wiadomości.",
        "status": "verified",
        "source_ids": [
          "wpb-corpus-verified"
        ],
        "external_use": true
      },
      {
        "id": "ev-wpb-005",
        "claim": "Stockholm Film Festival press materials identify Weronika Pérez Borjas as press assistant and later press secretary during the 2015 festival cycle.",
        "status": "verified",
        "source_ids": [
          "wpb-credits-verified"
        ],
        "external_use": true
      },
      {
        "id": "ev-wpb-006",
        "claim": "A verified catalogue record credits Weronika Pérez Borjas with the Polish translation of Susanna Isern's Oso cazamariposas / Niedźwiedź łowca motyli.",
        "status": "verified",
        "source_ids": [
          "wpb-credits-verified"
        ],
        "external_use": true
      },
      {
        "id": "ev-wpb-007",
        "claim": "A verified Krull Magazine record credits Weronika Pérez Borjas with styling work.",
        "status": "verified",
        "source_ids": [
          "wpb-credits-verified"
        ],
        "external_use": true
      },
      {
        "id": "ev-wpb-008",
        "claim": "The verified corpus includes interview and profile-writing work across music, culture, identity and social subjects.",
        "status": "verified",
        "source_ids": [
          "wpb-corpus-verified"
        ],
        "external_use": true
      }
    ],
    "positioning": {
      "headline": "Writer and reporter with verified work across cultural journalism, interviews, social reporting and long-form reportage",
      "functional_core": [
        "Research and reporting",
        "Interviewing and profile writing",
        "Long-form social and migration reportage",
        "Press and media relations",
        "Translation"
      ],
      "derived_from_evidence_ids": [
        "ev-wpb-001",
        "ev-wpb-002",
        "ev-wpb-004",
        "ev-wpb-005",
        "ev-wpb-006",
        "ev-wpb-008"
      ]
    },
    "verification_queue": [
      {
        "id": "wpb-current-employment",
        "question": "Confirm current employment and current professional role before using it in matching or applications.",
        "status": "open"
      },
      {
        "id": "wpb-current-location",
        "question": "Confirm current location; do not infer residence from historical Stockholm-based work.",
        "status": "open"
      },
      {
        "id": "wpb-spoken-languages",
        "question": "Confirm spoken-language proficiency separately from publication-language evidence.",
        "status": "open"
      },
      {
        "id": "wpb-education",
        "question": "Add source-backed education chronology before using education claims in applications.",
        "status": "open"
      },
      {
        "id": "wpb-tools",
        "question": "Add verified software and tool proficiency if it should be used in matching.",
        "status": "open"
      },
      {
        "id": "wpb-availability",
        "question": "Confirm current availability and engagement preferences.",
        "status": "open"
      }
    ]
  },
  "hy_filter_decision": "Auto",
  "trace": {
    "run_id": "cbcbfd5d-fe26-4034-aedb-3245ea7f9740",
    "mode": "R",
    "timestamp": "2026-10-06T15:57:52.869463+00:00",
    "environment": "Standalone",
    "piusite_usage": false,
    "hy_filter_usage": false,
    "hcc_authority": "HCC-Lite",
    "downing_street_loop_count": 0,
    "final_output_state": "OPEN",
    "process_id_validation_status": true,
    "last_pid_rev": "HRDM-R-20261006-0001-S09-A-R01-OPEN",
    "process_id": "HRDM-R-20261006-0001-S09-A-R01-OPEN",
    "runseq": 1,
    "step_process_ids": {
      "S01": "HRDM-R-20261006-0001-S01-A-R01-LOCK",
      "S02": "HRDM-R-20261006-0001-S02-A-R01-LOCK",
      "S03": "HRDM-R-20261006-0001-S03-A-R01-LOCK",
      "S04": "HRDM-R-20261006-0001-S04-A-R01-LOCK",
      "S05": "HRDM-R-20261006-0001-S05-A-R01-LOCK",
      "S06": "HRDM-R-20261006-0001-S06-A-R01-LOCK",
      "S07": "HRDM-R-20261006-0001-S07-A-R01-LOCK",
      "S08": "HRDM-R-20261006-0001-S08-A-R01-LOCK",
      "S09": "HRDM-R-20261006-0001-S09-A-R01-OPEN"
    },
    "outstanding_warnings": [],
    "bank_eligible_outputs": [],
    "hy_filter_evaluated": true,
    "hy_filter_activated": false
  },
  "constraints": [
    "Run the full HRDM-R sequence in canonical order.",
    "Do not invent candidate facts.",
    "Use only verified career sources and source-bound verified evidence as candidate facts.",
    "Private life, model memory, conversational impressions and search-only wishes are forbidden as candidate evidence.",
    "Separate job-ad facts from inference.",
    "Unknown candidate facts remain unknown.",
    "HCC-Lite must address structural honesty, overload, dignity, fairness, vulnerability sensitivity, non-deceptive framing and trace/accountability.",
    "Hybridianesque relevance is evaluated automatically. Activate only when the evidence-based validity threshold is met."
  ]
}
