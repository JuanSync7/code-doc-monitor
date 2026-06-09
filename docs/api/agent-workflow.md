---
cdm:
  audience: eng-guide
  fingerprint: ae25638d8e7f119d
  schema_version: 1.0.0
---
# agent-workflow

> The deterministic LangGraph remediation agent: the `Backend`-shaped entry
> (`backend`), the graph wiring + artifact selection/context (`graph`), the
> prompt library (`prompts`), the runtime/driver leaf (`runtime`), and the
> graph's shared state (`state`).

<!-- CDM:BEGIN symbols -->
| symbol | kind | signature |
|--------|------|-----------|
| AgentBackend | class | class AgentBackend |
| AgentBackend.__init__ | method | def __init__(self, cfg: AgentConfig, *, driver: Driver \| None = None, library: PromptLibrary \| None = None) -> None |
| AgentBackend._ensure_graph | method | def _ensure_graph(self) -> CompiledStateGraph |
| AgentBackend.propose | method | def propose(self, req: FixRequest) -> BackendResult |
| Artifact | class | class Artifact |
| Driver | variable | Driver = Callable[[str], str] |
| PACKAGED_PROMPTS_DIR | variable | PACKAGED_PROMPTS_DIR = Path(__file__).parent / 'prompts' |
| PromptLibrary | class | class PromptLibrary |
| PromptLibrary.__init__ | method | def __init__(self, prompts_dir: Path \| None = None) -> None |
| PromptLibrary.directory | method | def directory(self) -> Path |
| PromptLibrary.exists | method | def exists(self, name: str) -> bool |
| PromptLibrary.get | method | def get(self, name: str) -> str |
| RemediationState | class | class RemediationState(TypedDict, total=False) |
| _DEFAULT_MODEL | variable | _DEFAULT_MODEL = 'claude-sonnet-4-20250514' |
| _RETRY_NUDGE | variable | _RETRY_NUDGE = ... |
| __all__ | variable | __all__ = ['RemediationState'] |
| __all__ | variable | __all__ = ... |
| __all__ | variable | __all__ = ['AgentBackend', 'make_agent_backend'] |
| __all__ | variable | __all__ = ['Driver', 'resolve_driver'] |
| __all__ | variable | __all__ = ... |
| _claude_code_argv | function | def _claude_code_argv(cfg: AgentConfig, prompt: str) -> list[str] |
| _openai_chat_call | function | def _openai_chat_call(base_url: str, model: str, prompt: str, timeout: int, api_key: str \| None) -> str |
| _render_exemplars | function | def _render_exemplars(req: FixRequest) -> str |
| _strip_front_matter | function | def _strip_front_matter(text: str) -> str |
| _wrap | function | def _wrap(driver: Driver, label: str) -> Driver |
| build_graph | function | def build_graph(driver: Driver, library: PromptLibrary, cfg: AgentConfig) -> CompiledStateGraph |
| make_agent_backend | function | def make_agent_backend(cfg: AgentConfig, *, driver: Driver \| None = None) -> AgentBackend |
| render_context | function | def render_context(req: FixRequest) -> str |
| resolve_driver | function | def resolve_driver(cfg: AgentConfig) -> Driver |
| select_artifacts | function | def select_artifacts(req: FixRequest, cfg: AgentConfig, library: PromptLibrary) -> list[str] |
<!-- CDM:END symbols -->
