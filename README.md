# code-doc-monitor

A **standardized, reusable** system that keeps documentation in sync with the
code it describes — and, when it drifts, asks an LLM to **fix or invalidate** the
drift while logging every decision for human review.

It generalizes the `docsync` pattern (extract a code surface → fingerprint it →
detect drift against the docs) into a project-agnostic tool, and closes the loop
with automatic, auditable remediation.

```
config ──> extract ──> drift ──┬─> clean → exit 0
                               └─> LLM backend → FIX | INVALIDATE | ESCALATE
                                        │
                                        ├─ apply fix to the doc (opt-in, idempotent)
                                        ├─ append a ReviewRecord to the JSONL review log
                                        └─ emit the record to a central monitoring system
```

## Why

A detector that only **warns** still needs a human to act; a fixer that acts
**silently** can't be trusted. code-doc-monitor detects, auto-remediates with an
LLM, and records the **original drift + the proposed fix** so a person (or a
central dashboard) can audit what changed and why — a self-healing monitor that
still keeps a human in the review seat.

## How a project adopts it

Write a config that maps groups of code files — down to functions, line ranges,
or variables — onto **logical documents**, each tagged with an **audience**. The
canonical form is the `config/cdmon/` directory layout (an `index.yaml` plus
per-area unit files; `cdmon` auto-detects it with no `--config`); a single
`cdmon.yaml`/`.json` file is also supported as a back-compat path. Each document
carries an audience:

- `user-guide` — only the externally-visible surface matters; comment / local /
  private changes are *invalidated* (not drift).
- `eng-guide` — the implementation surface matters too; those changes *are*
  flagged.

```bash
cdmon init                 # write a config template (offline)
cdmon init --central URL --repo-id ID   # ...wired for HTTP reporting to a central server (sink=http + url + repo_id + auth_env + outbox); --token-env VAR (default CDMON_CENTRAL_TOKEN), --repo-url URL; ready to `cdmon register` + report (G-01)
cdmon doctor               # offline, read-only preflight: PASS/WARN/FAIL on config, documents, backend prereq, central wiring, optional extras; exit 0 unless a structural FAIL (absent runtime prereq/unset token = WARN, never FAIL; no network) (G-02)
cdmon new-doc <doc-id>     # scaffold a conformant, in-sync doc from config + code
cdmon surface              # dump the extracted per-document surface (debug)
cdmon lint [--fix]         # validate doc *structure* (Layout Standard); --fix stamps front matter
cdmon check                # detect *content* drift; non-zero exit on drift (the warning)
cdmon monitor --apply      # detect → LLM verdict → record → apply fix → re-check
cdmon monitor --ref SHA    # ...and stamp each record's source_sha provenance (else $CI_COMMIT_SHA; C-05)
cdmon sync-pr [--dry-run]  # heal docs + emit a unified-diff patch of the changed docs (the docs-PR content); --dry-run computes the same patch without touching the tree; --out FILE writes it
cdmon open-docs-pr [--dry-run]  # heal docs then open a docs MR (branch+commit+MR) via the default GitLab transport (stdlib urllib; from CI env); clean repo is a no-op; --dry-run prints the MR plan as JSON from a dry sync (no mutation, no network); --target/--ref set the target branch + provenance ref
cdmon should-sync [FILES...]  # loop-safety guard: exit 0 to proceed / 1 to skip a heal; skips when every changed file is a managed doc (a bot doc-only commit). `git diff --name-only | cdmon should-sync` (C-04)
cdmon report               # summarize the review log + resolved/unresolved counts (--verdict ESCALATE lists those records)
cdmon resolve REC --resolution accepted [--by NAME] [--text ...] [--note ...]  # record a human outcome (accepted|overridden|rejected|invalidated) as a separate append-only event linked to a review record; the review log stays immutable (K5)
cdmon promotions           # list promotion candidates: shapes (doc_id,drift_kind,audience) whose ≥N resolved records ALL share one DECISION (invalidated|rejected) — promotable to a deterministic rule the monitor applies with ZERO backend calls (--min-count N; --json) (D-05/D-06)
cdmon coverage             # doc-coverage % + gaps/waivers (--json; --fail-under N gates)
cdmon coverage --write     # write a deterministic manifest (payload + gap→owner suggestions) to .cdmon/coverage.json (idempotent; --write PATH for a custom path)
cdmon surface-gaps [--dry-run] [--provider gitlab|github]  # turn undocumented-public-symbol coverage gaps into a tracker issue (grouped by suggested owner); no gaps is a no-op; --dry-run prints the deterministic IssuePlan JSON without building/calling a transport; else opens the issue via the provider's stdlib-urllib transport (from CI env; loud if unset) (H-04)
cdmon register [--dry-run] # announce this repo to the central server: POST its identity (RegistrationPayload) to <central url>/repos (bearer from central.auth_env; stdlib only); --dry-run prints the payload without any network call (E-02)
cdmon schema               # emit the public ReviewRecord JSON schema
```

### Drop-in CI + a worked example (EPIC G)

- **`templates/ci/`** — copy-paste CI for adopters: `gitlab-ci.adopter.yml`
  (GitLab) and `github-actions.adopter.yml` (GitHub Actions), each with a
  `cdmon-gate` job (`doctor` → `check` → `lint`, offline) and a default-branch
  `cdmon-docs-pr` job (`should-sync` guard → `monitor --apply` → `open-docs-pr`).
  See `templates/ci/README.md`; set `CDMON_CENTRAL_TOKEN` as a CI secret (E-06). A
  repo test keeps the templates honest — they reference only real `cdmon`
  subcommands.
- **`examples/external-repo/`** — a small self-contained repo that ADOPTS cdmon
  (its own `src/widget.py` + `docs/api.md` + `cdmon.yaml`). Its test heals it and
  reports the healed records to an in-process central server (`TestClient`) with a
  bearer token, proving the whole client→server loop offline (the capstone, G-04).
  (See also `examples/multilang/` for cross-language extraction.)

## Document Layout Standard

Beyond keeping content in sync, code-doc-monitor standardizes **how a managed
doc is written** so every adopting project lays its docs out the same way: a
canonical skeleton (front matter → `#` title → `>` purpose → prose →
`CDM:BEGIN/END` regions), a managed front-matter schema
(`cdm.schema_version` / `audience` / `fingerprint`), and an HTML-twin pairing
rule (`X.md` → `X.html`, derived-not-edited, carrying an embedded source hash).
helium's `HELIUM:AUTOGEN … START/END` markers are a documented alias of the same
grammar. The standard is **machine-checked** — `cdmon lint` is a structure gate
orthogonal to `check`'s content gate (run both in CI) — and `cdmon new-doc`
scaffolds a conformant file. See [`docs/LAYOUT_STANDARD.md`](docs/LAYOUT_STANDARD.md).

## Backends (pluggable, offline by default)

The LLM backend is chosen entirely by config:

- `mock` — deterministic, offline; the default, and what the test suite uses.
- `claude-code` — runs a headless `claude -p` session as a subprocess.
- `api` — calls the Anthropic Messages API.
- `agent` — a deterministic **LangGraph** remediation workflow (see below).

Switching between them is a config edit, never a code change. The engine is
backend-agnostic: all four return the same `BackendResult` JSON contract.

## The LangGraph remediation agent

`backend.kind: agent` runs remediation as a deterministic LangGraph
`StateGraph` (`select → compose → invoke → parse`, with a bounded re-ask loop)
instead of a single monolithic prompt. Its prompt is **composed from separated
Markdown artifacts**, loaded *only when a node needs them*:

- [`AGENT.md`](code_doc_monitor/agent/prompts/AGENT.md) — the recipe + audience-aware judgement rules,
- [`PROTOCOL.md`](code_doc_monitor/agent/prompts/PROTOCOL.md) — the strict JSON verdict contract,
- [`TOOL.md`](code_doc_monitor/agent/prompts/TOOL.md) — the two fix shapes (loaded only for a healable drift),
- [`PERSONA.md`](code_doc_monitor/agent/prompts/PERSONA.md) — voice (loaded only when `use_persona`).

The agent's **runtime** is a second config-only choice — *the one knob the brief
asked for*: the agent uses the headless Claude Code CLI by default, and can be
pointed at an Anthropic API key or a local model endpoint with no code change:

```yaml
backend:
  kind: agent
agent:
  driver: claude-code            # headless `claude -p` (default)
  # driver: api                  # Anthropic API; key from $api_key_env
  # driver: local                # any OpenAI-compatible endpoint
  #   base_url: http://localhost:11434/v1
  model: claude-sonnet-4
  use_persona: true
  max_parse_retries: 1
```

The graph is fully deterministic (K10); only the injected runtime *driver*
touches a process or socket, so the whole workflow runs offline in tests (K4).
The agent ships behind an opt-in extra: `pip install -e '.[agent]'` (or `[dev]`).

## Central server (optional `[server]` extra)

The central side of the sink/registry is a FastAPI app in
`code_doc_monitor.server` that ingests repo registrations + review records over
the **same** versioned schemas the client sends — no DTOs. It ships behind an
opt-in extra (`pip install -e '.[server]'`) and is imported lazily, so the core
engine pulls in no `fastapi`. Routes:

| route | body → response |
|---|---|
| `POST /repos` | `RegistrationPayload` → `201 {repo_id}` |
| `POST /ingest` | `IngestEnvelope` → `202 {record_id}` (unknown repo → 404) |
| `GET /repos` | `list[RegisteredRepo]` |
| `GET /repos/{repo_id}/records` | `list[ReviewRecord]` (filter/paginate via query params) |
| `GET /repos/{repo_id}/health` | `RepoHealth` — computed metrics view |
| `GET /repos/{repo_id}/telemetry` | `RepoTelemetry` — per `(drift_kind, audience)` underperformer view (count, escalation_rate, override_rate) worst-first + promotion candidates (H-01) |

A malformed body is a `422` (pydantic against the shared model). Run it with
`cdmon-server` or `uvicorn code_doc_monitor.server.app:create_app --factory`.
Storage is an in-memory `Store` Protocol today; a Postgres store swaps in behind
the same Protocol later.

## Interactive editing — the Mapping page

The dashboard's per-repo **Mapping page** (`/repos/:repoId/mapping`) shows and
edits the repo's `config/cdmon/*.yaml` document↔code mapping from the browser:

- **View the config live.** Each document is a dropdown listing its `code_refs`
  (the documented surface — path + symbols/lines or "whole file") and its
  `context_refs` (generation-context references, shown distinctly). In-scope but
  **unlinked** source files appear as a flat list; **ignored** files sit in a
  closed `<details>` tab at the bottom.
- **File a mapping "ticket".** "Link to a document…" / "Edit mapping" opens a form
  — target document (existing or new id + path + audience), source file, scope
  (whole file / a `start-end` line range / specific symbols), the four doc-style
  category selections, and `context_refs`. Submitting stages a `config_edit`
  (nothing is written to disk yet); staged edits show as a pending list.
- **Generate / make live.** One button applies the staged edits to the on-disk
  units + index, scaffolds/heals the affected docs, and re-runs the sync so the
  page reflects the now-live state. Disk stays the git-tracked source of truth;
  the SQL store is the live mirror the dashboard reads.
- **One-click apply-fix.** On a drift ticket with a `FIX` verdict, an
  **"Apply fix (LLM)"** button applies the record's proposed fix to the doc on
  disk, records the acceptance, re-syncs, and shows the diff.

**`context_refs`** is a new unit-file key for sub-documents / sub-source-files the
author should glance through when generating a doc. It is **generation context
only** — surfaced to the authoring prompt, never counted in coverage or drift,
distinct from `code_refs`.

Try it on the demo: `demo/` ships with `scheduler.py` intentionally **unlinked**
— open the Mapping page, link it to a document via the ticket form, hit
**Generate**, and watch it become documented live. `demo/walkthrough.py` drives
the apply-fix and link→generate flows end-to-end, offline.

## Public schema

Every handled drift becomes a versioned `ReviewRecord` (the public contract for
the central monitoring system). The JSON Schema is generated from the model —
`cdmon schema` — and a snapshot lives at
[`docs/REVIEW_RECORD_SCHEMA.json`](docs/REVIEW_RECORD_SCHEMA.json).

## Dogfooding

code-doc-monitor monitors **its own** source against its own engineering docs:
the shipped [`config/cdmon/`](config/cdmon) dir layout (an `index.yaml` plus the
per-area unit files) maps this package's modules onto the docs under `docs/api/`
(with `schema.py` as a shared, multiply-referenced file). Run `cdmon check` here
(it auto-detects `config/cdmon/`) to see it in action; the dogfood is asserted in
`tests/test_dogfood.py`.

## Status

**Complete.** All slices CDM-00…CDM-10 are done: config + audience-aware
extraction + drift detection + heal + public schema + review log + central sinks
+ pluggable backends (mock / claude-code / api / **LangGraph agent**) + the
monitor orchestration and `cdmon` CLI + the Document Layout Standard (`lint` /
`new-doc`), with system/e2e tests and dogfooding. The suite is offline (mock
backend, no network), ruff + mypy clean, coverage ≥ 90% (322 tests). See
`.project/` for the spec, the binding constraints (K0–K10), the architecture, and
the slice-by-slice status board.

## Development

```bash
python3.11 -m venv .venv && .venv/bin/pip install -e '.[dev]'  # [dev] includes langgraph
.venv/bin/ruff format --check . && .venv/bin/ruff check .
.venv/bin/mypy code_doc_monitor
.venv/bin/pytest -q --cov=code_doc_monitor --cov-branch
```

The LangGraph agent backend is an opt-in extra; for a runtime-only install use
`pip install -e '.[agent]'` (the core engine and its `mock` default need neither).
The central FastAPI server is a second opt-in extra: `pip install -e '.[server]'`
(`[dev]` includes both extras so the gate exercises the server tests).

### Testing against a real LLM (CI/CD)

The default suite is **offline** (K4): a bare `pytest` excludes the `live_llm`
marker, so it never spawns a model. One opt-in end-to-end test
(`tests/test_live_llm.py`) drives a **real** backend — resolved from a config
file exactly like production — and asserts `monitor --apply` self-heals a doc in
a single pass:

```bash
# backend.kind comes from the config the test writes (CDMON_LIVE_BACKEND)
CDMON_LIVE_LLM=1 CDMON_LIVE_BACKEND=claude-code .venv/bin/pytest -m live_llm
```

[`.gitlab-ci.yml`](.gitlab-ci.yml) wires this as a two-gate pipeline: `tests:offline`
runs on every push/MR, and `tests:live-llm` runs the real-LLM test on a schedule
(and on-demand), gated on an `ANTHROPIC_API_KEY` CI/CD variable. This guards a
real-vs-mock divergence the offline suite can't see: a live model may return a
fix that fills *both* the region and whole-doc shapes at once, so `apply_fix`
prefers the whole-doc text (the only shape that refreshes the fingerprint) to
keep `monitor --apply` single-pass idempotent.
