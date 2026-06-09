---
cdm:
  audience: eng-guide
  fingerprint: 7f4741982ddac1f2
  region_hashes:
    symbols: 16216fadc6360d17
  schema_version: 1.0.0
---
# server

> EPIC G central server (engineering reference): the FastAPI ingest/query app
> (`app`), the persistence service over review records (`store`), and the
> SQLAlchemy schema + session/engine layer it sits on (`db`).

<!-- CDM:BEGIN symbols -->
| symbol | kind | signature |
|--------|------|-----------|
| AddCodeRefEdit | class | class AddCodeRefEdit(BaseModel) |
| ApplyFixResponse | class | class ApplyFixResponse(BaseModel) |
| Base | class | class Base(DeclarativeBase) |
| ConfigCodeRef | class | class ConfigCodeRef(BaseModel) |
| ConfigCodeRefRow | class | class ConfigCodeRefRow(Base) |
| ConfigContextRef | class | class ConfigContextRef(BaseModel) |
| ConfigDocument | class | class ConfigDocument(BaseModel) |
| ConfigDocumentRow | class | class ConfigDocumentRow(Base) |
| ConfigEdit | variable | ConfigEdit = ... |
| ConfigEditRow | class | class ConfigEditRow(Base) |
| CoverageIngest | class | class CoverageIngest(BaseModel) |
| CoverageSnapshotRow | class | class CoverageSnapshotRow(Base) |
| CreateDocEdit | class | class CreateDocEdit(BaseModel) |
| DocStyleOptions | class | class DocStyleOptions(BaseModel) |
| DocumentTree | class | class DocumentTree(BaseModel) |
| EditCodeRef | class | class EditCodeRef(BaseModel) |
| EditContextRef | class | class EditContextRef(BaseModel) |
| EditDocStyle | class | class EditDocStyle(BaseModel) |
| EditableConfigTree | class | class EditableConfigTree(BaseModel) |
| EditableDocument | class | class EditableDocument(BaseModel) |
| GenerateRequest | class | class GenerateRequest(BaseModel) |
| GenerateResponse | class | class GenerateResponse(BaseModel) |
| InMemoryStore | class | class InMemoryStore |
| InMemoryStore.__init__ | method | def __init__(self) -> None |
| InMemoryStore.add_config_edit | method | def add_config_edit(self, repo_id: str, edit: ConfigEdit, *, edit_id: str, created_at: str) -> None |
| InMemoryStore.add_coverage_snapshot | method | def add_coverage_snapshot(self, repo_id: str, captured_at: str, snapshot: dict) -> None |
| InMemoryStore.add_record | method | def add_record(self, repo_id: str, record: ReviewRecord) -> None |
| InMemoryStore.add_repo | method | def add_repo(self, payload: RegistrationPayload) -> None |
| InMemoryStore.add_resolution | method | def add_resolution(self, resolution: ResolutionRecord) -> None |
| InMemoryStore.add_sync_run | method | def add_sync_run(self, run: SyncRun) -> None |
| InMemoryStore.code_refs_for | method | def code_refs_for(self, repo_id: str, doc_id: str \| None = None, sync_kind: str \| None = None) -> list[ConfigCodeRef] |
| InMemoryStore.config_documents_for | method | def config_documents_for(self, repo_id: str, sync_kind: str \| None = None) -> list[ConfigDocument] |
| InMemoryStore.config_edits_for | method | def config_edits_for(self, repo_id: str, status: str \| None = None) -> list[StoredConfigEdit] |
| InMemoryStore.coverage_for | method | def coverage_for(self, repo_id: str) -> list[dict] |
| InMemoryStore.get_repo | method | def get_repo(self, repo_id: str) -> RegisteredRepo \| None |
| InMemoryStore.latest_sync_run | method | def latest_sync_run(self, repo_id: str, sync_kind: str \| None = None) -> SyncRun \| None |
| InMemoryStore.list_repos | method | def list_repos(self) -> list[RegisteredRepo] |
| InMemoryStore.mark_config_edits | method | def mark_config_edits(self, repo_id: str, edit_ids: list[str], status: str, *, at: str) -> None |
| InMemoryStore.records_for | method | def records_for(self, repo_id: str, *, verdict: str \| None = None, drift_kind: str \| None = None, audience: str \| None = None, doc_id: str \| None = None, limit: int \| None = None, offset: int = 0) -> list[ReviewRecord] |
| InMemoryStore.replace_config | method | def replace_config(self, repo_id: str, sync_kind: str, documents: list[ConfigDocument], code_refs: list[ConfigCodeRef]) -> None |
| InMemoryStore.repo_token_hash | method | def repo_token_hash(self, repo_id: str) -> str \| None |
| InMemoryStore.resolutions_for_repo | method | def resolutions_for_repo(self, repo_id: str, record_id: str \| None = None) -> list[ResolutionRecord] |
| InMemoryStore.sync_runs_for | method | def sync_runs_for(self, repo_id: str, sync_kind: str \| None = None) -> list[SyncRun] |
| RecordRow | class | class RecordRow(Base) |
| RegisteredRepo | class | class RegisteredRepo(BaseModel) |
| RemoveCodeRefEdit | class | class RemoveCodeRefEdit(BaseModel) |
| RepoHealth | class | class RepoHealth(BaseModel) |
| RepoRow | class | class RepoRow(Base) |
| RepoStatus | class | class RepoStatus(BaseModel) |
| RepoTelemetry | class | class RepoTelemetry(BaseModel) |
| ResolutionRow | class | class ResolutionRow(Base) |
| SetContextRefsEdit | class | class SetContextRefsEdit(BaseModel) |
| SetDocStyleEdit | class | class SetDocStyleEdit(BaseModel) |
| ShapeStat | class | class ShapeStat(BaseModel) |
| SqlStore | class | class SqlStore |
| SqlStore.__init__ | method | def __init__(self, engine: Engine) -> None |
| SqlStore._session | method | def _session(self) -> Session |
| SqlStore.add_config_edit | method | def add_config_edit(self, repo_id: str, edit: ConfigEdit, *, edit_id: str, created_at: str) -> None |
| SqlStore.add_coverage_snapshot | method | def add_coverage_snapshot(self, repo_id: str, captured_at: str, snapshot: dict) -> None |
| SqlStore.add_record | method | def add_record(self, repo_id: str, record: ReviewRecord) -> None |
| SqlStore.add_repo | method | def add_repo(self, payload: RegistrationPayload) -> None |
| SqlStore.add_resolution | method | def add_resolution(self, resolution: ResolutionRecord) -> None |
| SqlStore.add_sync_run | method | def add_sync_run(self, run: SyncRun) -> None |
| SqlStore.code_refs_for | method | def code_refs_for(self, repo_id: str, doc_id: str \| None = None, sync_kind: str \| None = None) -> list[ConfigCodeRef] |
| SqlStore.config_documents_for | method | def config_documents_for(self, repo_id: str, sync_kind: str \| None = None) -> list[ConfigDocument] |
| SqlStore.config_edits_for | method | def config_edits_for(self, repo_id: str, status: str \| None = None) -> list[StoredConfigEdit] |
| SqlStore.coverage_for | method | def coverage_for(self, repo_id: str) -> list[dict] |
| SqlStore.coverage_snapshots_for | method | def coverage_snapshots_for(self, repo_id: str) -> list[dict] |
| SqlStore.get_repo | method | def get_repo(self, repo_id: str) -> RegisteredRepo \| None |
| SqlStore.latest_sync_run | method | def latest_sync_run(self, repo_id: str, sync_kind: str \| None = None) -> SyncRun \| None |
| SqlStore.list_repos | method | def list_repos(self) -> list[RegisteredRepo] |
| SqlStore.mark_config_edits | method | def mark_config_edits(self, repo_id: str, edit_ids: list[str], status: str, *, at: str) -> None |
| SqlStore.records_for | method | def records_for(self, repo_id: str, *, verdict: str \| None = None, drift_kind: str \| None = None, audience: str \| None = None, doc_id: str \| None = None, limit: int \| None = None, offset: int = 0) -> list[ReviewRecord] |
| SqlStore.replace_config | method | def replace_config(self, repo_id: str, sync_kind: str, documents: list[ConfigDocument], code_refs: list[ConfigCodeRef]) -> None |
| SqlStore.repo_token_hash | method | def repo_token_hash(self, repo_id: str) -> str \| None |
| SqlStore.resolutions_for | method | def resolutions_for(self, record_id: str) -> list[ResolutionRecord] |
| SqlStore.resolutions_for_repo | method | def resolutions_for_repo(self, repo_id: str, record_id: str \| None = None) -> list[ResolutionRecord] |
| SqlStore.sync_runs_for | method | def sync_runs_for(self, repo_id: str, sync_kind: str \| None = None) -> list[SyncRun] |
| Store | class | class Store(Protocol) |
| Store.add_config_edit | method | def add_config_edit(self, repo_id: str, edit: ConfigEdit, *, edit_id: str, created_at: str) -> None |
| Store.add_coverage_snapshot | method | def add_coverage_snapshot(self, repo_id: str, captured_at: str, snapshot: dict) -> None |
| Store.add_record | method | def add_record(self, repo_id: str, record: ReviewRecord) -> None |
| Store.add_repo | method | def add_repo(self, payload: RegistrationPayload) -> None |
| Store.add_resolution | method | def add_resolution(self, resolution: ResolutionRecord) -> None |
| Store.add_sync_run | method | def add_sync_run(self, run: SyncRun) -> None |
| Store.code_refs_for | method | def code_refs_for(self, repo_id: str, doc_id: str \| None = None, sync_kind: str \| None = None) -> list[ConfigCodeRef] |
| Store.config_documents_for | method | def config_documents_for(self, repo_id: str, sync_kind: str \| None = None) -> list[ConfigDocument] |
| Store.config_edits_for | method | def config_edits_for(self, repo_id: str, status: str \| None = None) -> list[StoredConfigEdit] |
| Store.coverage_for | method | def coverage_for(self, repo_id: str) -> list[dict] |
| Store.get_repo | method | def get_repo(self, repo_id: str) -> RegisteredRepo \| None |
| Store.latest_sync_run | method | def latest_sync_run(self, repo_id: str, sync_kind: str \| None = None) -> SyncRun \| None |
| Store.list_repos | method | def list_repos(self) -> list[RegisteredRepo] |
| Store.mark_config_edits | method | def mark_config_edits(self, repo_id: str, edit_ids: list[str], status: str, *, at: str) -> None |
| Store.records_for | method | def records_for(self, repo_id: str, *, verdict: str \| None = None, drift_kind: str \| None = None, audience: str \| None = None, doc_id: str \| None = None, limit: int \| None = None, offset: int = 0) -> list[ReviewRecord] |
| Store.replace_config | method | def replace_config(self, repo_id: str, sync_kind: str, documents: list[ConfigDocument], code_refs: list[ConfigCodeRef]) -> None |
| Store.repo_token_hash | method | def repo_token_hash(self, repo_id: str) -> str \| None |
| Store.resolutions_for_repo | method | def resolutions_for_repo(self, repo_id: str, record_id: str \| None = None) -> list[ResolutionRecord] |
| Store.sync_runs_for | method | def sync_runs_for(self, repo_id: str, sync_kind: str \| None = None) -> list[SyncRun] |
| StoredConfigEdit | class | class StoredConfigEdit(BaseModel) |
| SyncRequest | class | class SyncRequest(BaseModel) |
| SyncRun | class | class SyncRun(BaseModel) |
| SyncRunRow | class | class SyncRunRow(Base) |
| _CONFIG_EDIT_ADAPTER | variable | _CONFIG_EDIT_ADAPTER: TypeAdapter[ConfigEdit] = TypeAdapter(ConfigEdit) |
| _CONFIG_SUBDIR | variable | _CONFIG_SUBDIR = ('config', 'cdmon') |
| _DEFAULT_BRANCH | variable | _DEFAULT_BRANCH = 'main' |
| _EDIT_CONFIG | variable | _EDIT_CONFIG = ConfigDict(extra='forbid', frozen=True) |
| _IGNORED_FILES_CAP | variable | _IGNORED_FILES_CAP = 200 |
| _LOG | variable | _LOG = logging.getLogger('code_doc_monitor.server') |
| _MODEL_CONFIG | variable | _MODEL_CONFIG = ConfigDict(extra='forbid', frozen=True) |
| __all__ | variable | __all__ = ... |
| __all__ | variable | __all__ = ... |
| __all__ | variable | __all__ = ... |
| __all__ | variable | __all__ = ... |
| __all__ | variable | __all__ = ... |
| _compute_health | function | def _compute_health(store: Store, repo_id: str) -> RepoHealth |
| _compute_status | function | def _compute_status(store: Store, repo_id: str) -> RepoStatus |
| _compute_telemetry | function | def _compute_telemetry(store: Store, repo_id: str) -> RepoTelemetry |
| _default_now | function | def _default_now() -> str |
| _default_static_dir | function | def _default_static_dir() -> Path \| None |
| _disk_editable_parts | function | def _disk_editable_parts(local_path: str \| None) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...], DocStyleOptions] |
| _json_type | function | def _json_type() -> TypeEngine[dict] |
| _new_edit_id | function | def _new_edit_id(repo_id: str, edit: ConfigEdit, now: str) -> str |
| _parse_iso | function | def _parse_iso(value: str) -> datetime |
| _registered_repo | function | def _registered_repo(row: RepoRow) -> RegisteredRepo |
| _run_migrations | function | def _run_migrations(url: str) -> None |
| _scan_doc_styles | function | def _scan_doc_styles(templates_root: Path) -> DocStyleOptions |
| build_standalone_app | function | def build_standalone_app(repo_root: Path, *, repo_id: str \| None = None, now: str) -> object |
| build_standalone_store | function | def build_standalone_store(repo_root: Path, *, repo_id: str \| None = None, now: str) -> InMemoryStore |
| create_all | function | def create_all(engine: Engine) -> None |
| create_app | function | def create_app(store: Store \| None = None, *, static_dir: Path \| None = None, clock: Callable[[], str] = _default_now) -> FastAPI |
| effective_identity | function | def effective_identity(payload: RegistrationPayload) -> RepoIdentity |
| engine_from_url | function | def engine_from_url(url: str) -> Engine |
| hash_token | function | def hash_token(token: str) -> str |
| main | function | def main() -> None |
| resolve_repo_id | function | def resolve_repo_id(repo_root: Path, repo_id: str \| None) -> str |
| store_from_env | function | def store_from_env() -> Store |
<!-- CDM:END symbols -->
