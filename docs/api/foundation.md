---
cdm:
  audience: eng-guide
  fingerprint: 083db089a2e0acf8
  region_hashes:
    symbols: 892e08537c988511
  schema_version: 1.0.0
---
# code-doc-monitor — foundation (engineering reference)

> Auto-maintained by code-doc-monitor itself (dogfood). The prose is human;
> the symbol table below is generated from the code and kept in sync.

<!-- CDM:BEGIN symbols -->
| symbol | kind | signature |
|--------|------|-----------|
| AgentConfig | class | class AgentConfig(BaseModel) |
| Audience | class | class Audience(str, Enum) |
| BackendConfig | class | class BackendConfig(BaseModel) |
| BackendError | class | class BackendError(CodeDocMonitorError) |
| CDMON_CONFIG_VERSION | variable | CDMON_CONFIG_VERSION = '2.0.0' |
| CONFIG_TEMPLATE | variable | CONFIG_TEMPLATE = ... |
| CentralConfig | class | class CentralConfig(BaseModel) |
| CodeDocMonitorError | class | class CodeDocMonitorError(Exception) |
| CodeRef | class | class CodeRef(BaseModel) |
| ConfigBundle | class | class ConfigBundle(BaseModel) |
| ConfigBundle.unit_for_document | method | def unit_for_document(self, doc_id: str) -> UnitFile \| None |
| ConfigBundle.unit_for_path | method | def unit_for_path(self, repo_relative_path: str) -> UnitFile \| None |
| ConfigError | class | class ConfigError(CodeDocMonitorError) |
| ContextRef | class | class ContextRef(BaseModel) |
| CoverageConfig | class | class CoverageConfig(BaseModel) |
| DEFAULT_CENTRAL_TOKEN_ENV | variable | DEFAULT_CENTRAL_TOKEN_ENV = 'CDMON_CENTRAL_TOKEN' |
| DOC_STYLE_TEMPLATE | variable | DOC_STYLE_TEMPLATE = ... |
| DocStyleFrontmatter | class | class DocStyleFrontmatter(BaseModel) |
| DocStyleFrontmatter._version_and_kind | method | def _version_and_kind(self) -> DocStyleFrontmatter |
| DocStyleMap | class | class DocStyleMap(BaseModel) |
| DocStyleMap.style_for | method | def style_for(self, doc_id: str) -> DocStyleSelection |
| DocStyleMapping | class | class DocStyleMapping(BaseModel) |
| DocStyleMapping.selection | method | def selection(self) -> DocStyleSelection |
| DocStyleSelection | class | class DocStyleSelection(BaseModel) |
| DocumentSpec | class | class DocumentSpec(BaseModel) |
| DocumentSpec._context_refs_paths_unique | method | def _context_refs_paths_unique(self) -> DocumentSpec |
| DocumentSpec._region_modes_reference_declared_regions | method | def _region_modes_reference_declared_regions(self) -> DocumentSpec |
| DocumentSpec.mode_for | method | def mode_for(self, region_id: str) -> RegionMode |
| DriftError | class | class DriftError(CodeDocMonitorError) |
| EXAMPLE_UNIT_STEM | variable | EXAMPLE_UNIT_STEM = 'example' |
| ExtractionError | class | class ExtractionError(CodeDocMonitorError) |
| IGNORE_TEMPLATE | variable | IGNORE_TEMPLATE = ... |
| INDEX_TEMPLATE | variable | INDEX_TEMPLATE = ... |
| IgnoreFile | class | class IgnoreFile(BaseModel) |
| IgnoreFrontmatter | class | class IgnoreFrontmatter(BaseModel) |
| IgnoreFrontmatter._version_must_match | method | def _version_must_match(self) -> IgnoreFrontmatter |
| IndexFile | class | class IndexFile(BaseModel) |
| IndexFrontmatter | class | class IndexFrontmatter(BaseModel) |
| IndexFrontmatter._version_must_match | method | def _version_must_match(self) -> IndexFrontmatter |
| IndexUnitRef | class | class IndexUnitRef(BaseModel) |
| InventoryError | class | class InventoryError(CodeDocMonitorError) |
| MonitorConfig | class | class MonitorConfig(BaseModel) |
| ProposedFix | class | class ProposedFix(BaseModel) |
| RESERVED_UNIT_STEMS | variable | RESERVED_UNIT_STEMS: frozenset[str] = frozenset({'index', 'ignore', 'doc-style'}) |
| RegionColumn | class | class RegionColumn(BaseModel) |
| RegionMode | class | class RegionMode(str, Enum) |
| RegionTemplate | class | class RegionTemplate(BaseModel) |
| STYLE_CATEGORIES | variable | STYLE_CATEGORIES: tuple[tuple[str, str], ...] = ... |
| SchemaError | class | class SchemaError(CodeDocMonitorError) |
| SyncError | class | class SyncError(CodeDocMonitorError) |
| TransportError | class | class TransportError(CodeDocMonitorError) |
| UNIT_TEMPLATE | variable | UNIT_TEMPLATE = ... |
| UnitFile | class | class UnitFile(BaseModel) |
| UnitFile._validate_scope | method | def _validate_scope(self) -> UnitFile |
| UnitFrontmatter | class | class UnitFrontmatter(BaseModel) |
| UnitFrontmatter._version_must_match | method | def _version_must_match(self) -> UnitFrontmatter |
| V2_TEMPLATES | variable | V2_TEMPLATES: dict[str, str] = ... |
| Verdict | class | class Verdict(str, Enum) |
| WaiverEntry | class | class WaiverEntry(BaseModel) |
| _DEFAULT_EXCLUDE | variable | _DEFAULT_EXCLUDE: tuple[str, ...] = ('**/.*/**', '**/__pycache__/**', '**/.venv/**') |
| _DEFAULT_INCLUDE | variable | _DEFAULT_INCLUDE: tuple[str, ...] = ('**/*.py',) |
| _FM_RE | variable | _FM_RE = ... |
| _MODEL_CONFIG | variable | _MODEL_CONFIG = ConfigDict(extra='forbid', frozen=True) |
| _OFFLINE_CENTRAL_BLOCK | variable | _OFFLINE_CENTRAL_BLOCK = ... |
| _UNITS_BLOCK_RE | variable | _UNITS_BLOCK_RE = ... |
| _UPDATED_LINE_RE | variable | _UPDATED_LINE_RE = re.compile('^updated:[^\\\\n]*$', re.MULTILINE) |
| _V2_MODEL_CONFIG | variable | _V2_MODEL_CONFIG = ... |
| __all__ | variable | __all__ = ... |
| __all__ | variable | __all__ = ... |
| __all__ | variable | __all__ = ... |
| __all__ | variable | __all__ = ... |
| __all__ | variable | __all__ = ... |
| _coderef_to_yaml | function | def _coderef_to_yaml(ref: CodeRef) -> dict |
| _contextref_to_yaml | function | def _contextref_to_yaml(ref: ContextRef) -> dict |
| _deepest_unit_for_parts | function | def _deepest_unit_for_parts(units: tuple[UnitFile, ...], file_parts: tuple[str, ...]) -> UnitFile \| None |
| _dir_parts | function | def _dir_parts(p: str) -> tuple[str, ...] |
| _document_to_yaml | function | def _document_to_yaml(doc: DocumentSpec) -> dict |
| _fill | function | def _fill(template: str, *, repo: str, now: str) -> str |
| _find_doc_index | function | def _find_doc_index(unit: UnitFile, doc_id: str) -> int |
| _is_ancestor | function | def _is_ancestor(ancestor: tuple[str, ...], descendant: tuple[str, ...]) -> bool |
| _load_v2_yaml | function | def _load_v2_yaml(path: Path) -> tuple[dict, str] |
| _missing_template_files | function | def _missing_template_files(selection: DocStyleSelection, templates_root: Path, *, where: str) -> list[str] |
| _now | function | def _now() -> str |
| _parse_v2_body | function | def _parse_v2_body(body: str, path: Path) -> dict |
| _render_units_block | function | def _render_units_block(filenames: list[str]) -> str |
| _replace_documents | function | def _replace_documents(unit: UnitFile, documents: tuple[DocumentSpec, ...]) -> UnitFile |
| _resolve_repo_root | function | def _resolve_repo_root(config_dir: Path, root: str) -> Path |
| _scan_unit_files | function | def _scan_unit_files(config_dir: Path) -> list[str] |
| _selection_to_yaml | function | def _selection_to_yaml(selection: DocStyleSelection) -> dict[str, str] |
| _split_frontmatter | function | def _split_frontmatter(text: str, where: Path) -> tuple[dict, str] |
| _yaml_scalar | function | def _yaml_scalar(value: str) -> str |
| _yaml_scalar | function | def _yaml_scalar(value: str) -> str |
| add_code_ref | function | def add_code_ref(unit: UnitFile, doc_id: str, ref: CodeRef) -> UnitFile |
| central_config_template | function | def central_config_template(*, url: str, repo_id: str, token_env: str = DEFAULT_CENTRAL_TOKEN_ENV, repo_url: str \| None = None) -> str |
| dump_doc_style | function | def dump_doc_style(doc_style: DocStyleMap, *, now: str) -> str |
| dump_unit_file | function | def dump_unit_file(unit: UnitFile, *, now: str) -> str |
| effective_coverage | function | def effective_coverage(bundle: ConfigBundle, repo_root: Path) -> CoverageConfig |
| gitignore_to_globs | function | def gitignore_to_globs(text: str) -> tuple[str, ...] |
| load_bundle | function | def load_bundle(config_dir: Path) -> ConfigBundle |
| load_config | function | def load_config(path: Path) -> MonitorConfig |
| load_config_dir | function | def load_config_dir(config_dir: Path) -> MonitorConfig |
| load_doc_style | function | def load_doc_style(path: Path, *, templates_root: Path) -> DocStyleMap |
| load_ignore_file | function | def load_ignore_file(path: Path) -> IgnoreFile |
| load_index_file | function | def load_index_file(path: Path) -> IndexFile |
| load_unit_file | function | def load_unit_file(path: Path) -> UnitFile |
| read_style_guidance | function | def read_style_guidance(selection: DocStyleSelection, templates_root: Path) -> str |
| regenerate_index | function | def regenerate_index(config_dir: Path) -> str |
| remove_code_ref | function | def remove_code_ref(unit: UnitFile, doc_id: str, path: str) -> UnitFile |
| resolve_repo_root | function | def resolve_repo_root(config_dir: Path, root: str) -> Path |
| resolve_style_files | function | def resolve_style_files(selection: DocStyleSelection, templates_root: Path) -> dict[str, Path] |
| scaffold_config_dir | function | def scaffold_config_dir(config_dir: Path, *, repo: str, now: str) -> None |
| set_context_refs | function | def set_context_refs(unit: UnitFile, doc_id: str, refs: tuple[ContextRef, ...]) -> UnitFile |
| unit_for_path | function | def unit_for_path(bundle: ConfigBundle, repo_relative_path: str) -> UnitFile \| None |
| upsert_document | function | def upsert_document(unit: UnitFile, doc: DocumentSpec) -> UnitFile |
| write_index | function | def write_index(config_dir: Path, text: str) -> None |
| write_template | function | def write_template(path: Path, content: str \| None = None) -> None |
<!-- CDM:END symbols -->
