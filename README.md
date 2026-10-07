# Objekts API

A read-only **FastAPI** service that exposes the "objekts" (COSMO collectible collections/drops) data used by the [cosmo-web](https://github.com/teamreflex/cosmo-web) repository, so it can be easily integrated into other projects.

## What this project does

The original `cosmo-web` monorepo (the web app / indexer behind Apollo) stores objekts information in Postgres schemas and indexes it into Typesense via its `typesense-import` app. That internal data model is not directly usable from external projects.

This API wraps that same data source and serves it as clean, documented JSON endpoints:

- **Proxy mode (default):** fetches objekt data from Apollo's public endpoints (`https://apollo.cafe`).
- **Typesense mode (optional):** queries a Typesense collection directly, using the schema mirrored from `packages/database/src/indexer/schema.ts` in the original repo — enabling fuzzy search and facets by artist, member, season, class, etc.

All Pydantic models (`Objekt`, `ObjektListResponse`, facets) mirror the shapes used by `cosmo-web`, including its pagination contract (`total`, `hasNext`, `nextStartAfter`, `objekts`).

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/health` | Service status check |
| `GET` | `/objekts` | Paginated list/search. Query params: `search`, `artist`, `member`, `season`, `class`, `page`, `per_page` |
| `GET` | `/objekts/{slug}` | Full details of a single objekt |

CORS middleware is enabled so the API can be consumed directly from frontend or backend projects.

## Getting started

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Configure via environment variables (prefix `COSMO_API_`) or a `.env` file:

```env
COSMO_API_APOLLO_BASE_URL=https://apollo.cafe

# Optional — direct Typesense access:
COSMO_API_TYPESENSE_URL=http://localhost:8108
COSMO_API_TYPESENSE_KEY=<search-only key created by typesense-import>
COSMO_API_TYPESENSE_COLLECTION=collections

# In-memory cache TTL (seconds)
COSMO_API_CACHE_TTL_SECONDS=300
```

Interactive docs are available at `http://localhost:8000/docs` once running.

## Credits & References

This is an unofficial, read-only companion project. All data, the objekts concept, and the underlying schema belong to the authors of the original repository:

- **Original repository:** [teamreflex/cosmo-web](https://github.com/teamreflex/cosmo-web)
- **Author:** Reflex (teamreflex)
- **License of original work:** MIT License — Copyright (c) Reflex
- **Key sources referenced:**
  - `packages/database/src/indexer/schema.ts` — Typesense collection schema (mirrored in [`app/models.py`](app/models.py))
  - `apps/typesense-import` — indexer that populates the `collections` index
  - Apollo public API (`https://apollo.cafe/api/objekts/...`) — default upstream data source

This project is not affiliated with or endorsed by MODHAUS or COSMO.
