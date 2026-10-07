# PR: docs: rewrite README in English with project overview and credits to cosmo-web

## Proposed PR title

```
docs: rewrite README in English with project overview, usage, and credits to teamreflex/cosmo-web
```

## Proposed PR description (paste into GitHub)

---

### Summary

Rewrites `README.md` in English so the repository clearly explains what the project is, how to run it, and gives proper credit and references to the original upstream repository, [teamreflex/cosmo-web](https://github.com/teamreflex/cosmo-web).

### Changes

- **Project overview** — Explains that this is a read-only **FastAPI** service exposing the "objekts" (COSMO collectible collections/drops) data used by `cosmo-web`, intended for reuse in other projects.
- **Data-source documentation** — Describes both consumption modes:
  - *Proxy mode (default):* fetches from Apollo's public endpoints (`https://apollo.cafe/api/objekts/...`).
  - *Typesense mode (optional):* direct queries against the collection indexed by the original repo's `apps/typesense-import`.
- **Endpoints table** — Documents `GET /health`, `GET /objekts` (with `search`, `artist`, `member`, `season`, `class`, `page`, `per_page` params), and `GET /objekts/{slug}`, plus the CORS note for third-party integration.
- **Getting started** — Install/run instructions and all `COSMO_API_*` environment variables, including cache TTL.
- **Credits & References** — New section crediting:
  - Original repository: `teamreflex/cosmo-web` (author: Reflex / teamreflex, MIT License)
  - Key sources mirrored: `packages/database/src/indexer/schema.ts` and `apps/typesense-import`
  - Disclaimer of non-affiliation with MODHAUS or COSMO.

### Commits included

| Commit | Message |
|--------|---------|
| `81b504e` | Rewrite README in English: project overview, usage, and credits to teamreflex/cosmo-web |

### Files changed

- `README.md` (+62 / -1)

### Notes for reviewers

- Documentation-only change; no code or behavior modified.
- The README is written entirely in **English**.

---

## How to open this PR (when remote access is available)

The sandbox has no git remote configured and no GitHub token, so the push could not be performed from here. From a machine authenticated with GitHub (`gh auth login`), run:

```bash
git checkout -b docs/readme-english 81b504e
git remote add origin https://github.com/<owner>/<repo>.git
git push -u origin docs/readme-english

gh pr create \
  --base main \
  --head docs/readme-english \
  --title "docs: rewrite README in English with project overview, usage, and credits to teamreflex/cosmo-web" \
  --body-file PULL_REQUEST.md
```

(Or simply paste the description above into the GitHub "New pull request" UI.)
