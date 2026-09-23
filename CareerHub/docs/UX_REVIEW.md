# CareerHub UX review — 2026-09-23

## UX objective

Weronika should be able to use CareerHub without understanding GitHub Actions, HRDM implementation details, APIs, YAML, JSON or the repository architecture.

Target interaction:

**see jobs → click Analyze → press Submit → download/edit Word draft**

## Main friction found in v1

### 1. The interface exposed backend concepts
The old control room asked the user to open Actions, select a workflow, choose lanes and later locate an artifact.

**Change:** Actions are now a backend/advanced control. The main interface uses direct job rows and issue-driven Analyze requests.

### 2. Too many decisions before value
The user had to decide between core/adjacent/bridge before even seeing a job.

**Change:** jobs are presented in plain-language groups. The lane is automatically carried into an Analyze request when the job came from CareerHub.

### 3. Numeric score dominated the board
A 0–100 sourcing score looked more authoritative than it is.

**Change:** numeric triage stays in the data layer. The normal UI uses relative labels such as Top lead / Good option / Explore within each lane.

### 4. No one-click path from lead to analysis
A user had to copy a URL, navigate to Actions and paste it into a workflow form.

**Change:** every generated job row now contains an **Analyze →** link that pre-populates a CareerHub request.

### 5. Jobs found elsewhere had no friendly entry point
The direct workflow was technically capable but not approachable.

**Change:** an **Analyze any job** GitHub Issue Form asks only for URL, purpose/lane and optional ad text.

### 6. The application pack appeared somewhere else
The user had to understand workflow runs and artifacts.

**Change:** the issue-driven workflow comments on the job request with a direct link to the completed run and download instructions.

### 7. Profile review required YAML
The actual candidate profile was machine-readable but poor for human review.

**Change:** `profile/PROFILE_REVIEW.md` presents confirmed and missing information in plain language.

### 8. Technical configuration competed with the core task
Sources, API setup, HRDM internals and privacy rules were visible in the primary flow.

**Change:** technical material is moved behind an **Advanced / maintainer controls** disclosure.

## Information architecture after review

### Primary surface
`CareerHub/CONTROL_ROOM.md`

Contains only:
- latest refresh state
- quick shortlist
- job groups
- Analyze actions
- profile review link
- simple explanation of what happens next

### Secondary surface
One CareerHub job-request issue = one application case file.

### Output
Temporary downloadable HRDM + DOCX pack.

### Maintainer layer
Setup, providers, HRDM specification, source configuration, validation and direct workflows.

## Security / usability trade-off

The one-click Analyze workflow can consume secret-backed services. On a public repository it therefore runs only for the owner/members/collaborators.

This adds one **one-time** maintainer action—add Weronika as collaborator—but removes repeated technical friction from every application.

## Remaining UX dependencies

- first real job scan should be reviewed for relevance
- profile reconciliation with Weronika should be completed
- optional OpenAI API key is needed for fully automated HRDM/research/writing
- job-board relevance should be tuned after seeing real results

No frontend application is required for the current workflow. If GitHub itself later becomes the dominant remaining friction, CareerHub can be promoted to a small authenticated web control room while keeping the same backend/data model.


## Production privacy conclusion

The UX target is now simple enough for regular use, but the public repository creates a structural privacy trade-off: an issue-based application request is visible publicly.

The preferred long-term architecture is therefore:

**public WPB archive → private CareerHub operating repository**

The private repository can use the same control-room, issue and workflow model without exposing job targets or application history.

This is not a redesign of CareerHub. It is a deployment decision that removes the last major usability/privacy compromise.
