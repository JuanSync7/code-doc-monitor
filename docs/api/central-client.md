---
cdm:
  audience: eng-guide
  fingerprint: d1a851a83c2edece
  region_hashes:
    symbols: 0f7f4c00b985b0ce
  schema_version: 1.0.0
---
# central-client

> The central-system client side (EPIC E/G): the per-repo registry/identity that
> stamps which repo a review record came from before it is shipped to the
> central ingest endpoint.

<!-- CDM:BEGIN symbols -->
| symbol | kind | signature |
|--------|------|-----------|
| GitInfo | class | class GitInfo(BaseModel) |
| HttpRegisterTransport | class | class HttpRegisterTransport |
| HttpRegisterTransport.__init__ | method | def __init__(self, url: str, auth_env: str \| None = None, *, http: _RegisterHttp \| None = None) -> None |
| HttpRegisterTransport.register | method | def register(self, payload: RegistrationPayload) -> dict |
| HttpSyncTransport | class | class HttpSyncTransport |
| HttpSyncTransport.__init__ | method | def __init__(self, url: str, auth_env: str \| None = None, *, http: _RegisterHttp \| None = None) -> None |
| HttpSyncTransport.sync | method | def sync(self, repo_id: str, *, mode: str) -> dict |
| RegisterTransport | class | class RegisterTransport(Protocol) |
| RegisterTransport.register | method | def register(self, payload: RegistrationPayload) -> dict |
| RegistrationPayload | class | class RegistrationPayload(BaseModel) |
| SyncResult | class | class SyncResult(BaseModel) |
| _CONFIG_SUBDIR | variable | _CONFIG_SUBDIR = ('config', 'cdmon') |
| _GitRunner | variable | _GitRunner = Callable[[list[str], Path], str] |
| _MODEL_CONFIG | variable | _MODEL_CONFIG = ConfigDict(extra='forbid', frozen=True) |
| _MODEL_CONFIG | variable | _MODEL_CONFIG = ConfigDict(extra='forbid', frozen=True) |
| _MODES | variable | _MODES = ('git', 'local') |
| _RegisterHttp | class | class _RegisterHttp(Protocol) |
| _RegisterHttp.request | method | def request(self, method: str, url: str, *, body: dict \| None, token: str) -> dict |
| _UrllibRegisterHttp | class | class _UrllibRegisterHttp |
| _UrllibRegisterHttp.request | method | def request(self, method: str, url: str, *, body: dict \| None, token: str) -> dict |
| __all__ | variable | __all__ = ... |
| __all__ | variable | __all__ = ... |
| _build_rows | function | def _build_rows(bundle: object, repo_id: str, *, mode: str, ref: str \| None, now: str) -> tuple[tuple[ConfigDocument, ...], tuple[ConfigCodeRef, ...]] |
| _coverage_percent | function | def _coverage_percent(bundle: object, config_dir: Path) -> float |
| _default_run_git | function | def _default_run_git(args: list[str], cwd: Path) -> str |
| _drift_summary | function | def _drift_summary(report: DriftReport, coverage_percent: float) -> dict |
| _git_info | function | def _git_info(local_path: Path, default_branch: str, *, run_git: _GitRunner) -> GitInfo |
| _open_repo | function | def _open_repo(local_path: Path, *, mode: str, branch: str, run_git: _GitRunner) -> Iterator[tuple[object, Path, GitInfo]] |
| read_config_at | function | def read_config_at(local_path: Path, *, mode: str, branch: str, now: str, run_git: _GitRunner = _default_run_git) -> tuple[object, Path, GitInfo] |
| register_repo | function | def register_repo(identity: RepoIdentity, *, url: str, auth_env: str \| None = None, transport: RegisterTransport \| None = None, dry_run: bool = False, default_branch: str \| None = None, description: str \| None = None, auth_token: str \| None = None) -> dict \| None |
| repo_identity_from_config | function | def repo_identity_from_config(cfg: CentralConfig) -> RepoIdentity |
| run_sync | function | def run_sync(local_path: Path, repo_id: str, *, mode: str, default_branch: str = 'main', now: str, run_git: _GitRunner = _default_run_git) -> SyncResult |
| sync_repo_remote | function | def sync_repo_remote(repo_id: str, *, mode: str, url: str, auth_env: str \| None = None, transport: HttpSyncTransport \| None = None) -> dict |
<!-- CDM:END symbols -->
