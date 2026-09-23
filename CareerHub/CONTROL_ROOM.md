# CareerHub

## Find a job. Click **Analyze**. Edit the Word draft.

**Status:** ready · jobs refresh automatically on weekdays

You normally only need to do one of these two things:

### I want to see jobs CareerHub found
The live job board will appear here after the first scheduled/manual refresh.

**[Refresh jobs now →](https://github.com/Hybrismannen/wpb/actions/workflows/careerhub-scan.yml)**

### I already found a job somewhere else
**[Analyze any job →](https://github.com/Hybrismannen/wpb/issues/new?template=careerhub-analyze-job.yml)**

Paste the link, choose why you are considering the job, and press **Submit new issue**.

CareerHub then handles the HRDM analysis, employer/role research and Word draft in the background.

---

## What happens after **Analyze**

1. CareerHub reads the public job advertisement.
2. It runs the full HRDM-R analysis.
3. It compares the role only with verified/supplied candidate evidence.
4. It creates an application strategy and editable Word draft.
5. A comment appears on the request with a link to the finished pack.

**You do not need to open GitHub Actions or understand the technical files.**

## The three kinds of jobs CareerHub looks for

| Type | What it means |
|---|---|
| **Career-track** | Writing, journalism, editorial, communications, press, research, cultural/NGO work |
| **Adjacent** | Content, coordination, research support, project/communications work, translation/localisation |
| **Extra-income / flexible** | Part-time, temporary, admin, support, reception, event/cultural venue and other practical work |

A lower-seniority role is not treated as a bad match simply because it is below the ceiling of Weronika's experience. The system evaluates it according to **why she is considering it**.

## My profile

CareerHub currently uses the verified WPB archive plus a public-safe candidate profile.

**[Review what CareerHub currently knows →](profile/PROFILE_REVIEW.md)**

Several current details still need Weronika's confirmation, especially languages, current status, tools, availability and preferred geography.

---

<details>
<summary><strong>Advanced / maintainer controls</strong></summary>

- [Refresh jobs manually](https://github.com/Hybrismannen/wpb/actions/workflows/careerhub-scan.yml)
- [Direct HRDM drill workflow](https://github.com/Hybrismannen/wpb/actions/workflows/careerhub-drill.yml)
- [One-time setup / optional APIs](SETUP.md)
- [Provider/source matrix](docs/SOURCE_MATRIX.md)
- [Full workflow](docs/WORKFLOW.md)
- [HRDM-R specification](hrdm/HRDM_R_v6.3.md)
- [Privacy rules](PRIVACY.md)

The numeric sourcing score is intentionally hidden from the normal interface. It is only an internal shortlist heuristic. The real role analysis happens after **Analyze**.

</details>
