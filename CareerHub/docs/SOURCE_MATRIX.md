# CareerHub source matrix

Provider integration is deliberately based on documented public access rather than brittle scraping.

| Source | CareerHub mode | Credentials | Notes |
|---|---|---|---|
| Arbetsförmedlingen JobSearch / Platsbanken | Public API | None | Primary Swedish source. JobSearch is public/open and exposes current Platsbanken ads. |
| Remotive | Public API | None | Remote jobs; CareerHub fetches once and filters locally to respect request guidance. Attribution/link-back retained. |
| Remote OK | Public JSON | None | Public JSON/RSS feeds. Attribution/link-back retained. |
| We Work Remotely | Public RSS | None | Public RSS feed. Attribution/link-back retained. |
| Adzuna | REST API | APP_ID + APP_KEY | Optional. API terms permit personal research within documented limits. |
| Jooble | REST API | Regional API key | Optional. Keys/endpoints are region-specific; no US fallback for Swedish searches. |
| Indeed | Partner/manual | Partner access if available | No general scraping. Use search manually and drill a selected public URL; partner integration can be added later. |
| Monster | Manual | None | No general public job-seeker API assumed. Use manual search + URL drill. |
| Ideella Jobb | Manual | None | High-value Swedish nonprofit source; no public API assumed. |
| Jobbland | Manual | None | Manual search + URL drill. |
| LinkedIn Jobs | Manual | None | No scraping/login automation; selected URLs may be drilled if publicly retrievable. |

## Official documentation / source pages

- Arbetsförmedlingen open APIs: https://arbetsformedlingen.se/other-languages/english-engelska/about-the-website/apis-and-open-data
- JobSearch open-data description: https://data.arbetsformedlingen.se/dataservice/jobsearch/
- JobSearch API: https://jobsearch.api.jobtechdev.se
- Indeed partner documentation: https://docs.indeed.com/
- Remotive public API: https://remotive.com/remote-jobs/api
- Remote OK public feeds: https://remoteok.com/faq
- We Work Remotely RSS: https://weworkremotely.com/remote-job-rss-feed
- Adzuna API: https://developer.adzuna.com/
- Jooble API: https://jooble.org/api/about
- Ideella Jobb: https://ideellajobb.se/
- Jobbland: https://jobbland.se/

## Design principle

CareerHub does not treat “can be scraped” as equivalent to “should be integrated”.

Where a source does not expose a suitable public job-search interface, CareerHub falls back to:
1. human search on the source,
2. selected job URL,
3. public-page drill if permitted,
4. pasted job text if retrieval is blocked.

That keeps the workflow durable and avoids creating a system that depends on bypassing provider controls.
