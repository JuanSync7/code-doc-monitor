---
cdm:
  audience: eng-guide
  fingerprint: 532590dbc66e0562
  schema_version: 1.0.0
---
# learning

> EPIC F learning loop: detect near-duplicate gaps/records (`similar`) and
> promote recurring, human-approved waivers and fixes into reusable config
> suggestions (`promotion`).

<!-- CDM:BEGIN symbols -->
| symbol | kind | signature |
|--------|------|-----------|
| Exemplar | class | class Exemplar(BaseModel) |
| FEATURE_WEIGHTS | variable | FEATURE_WEIGHTS: dict[str, float] = ... |
| PROMOTABLE_RESOLUTIONS | variable | PROMOTABLE_RESOLUTIONS: frozenset[Resolution] = ... |
| PromotionCandidate | class | class PromotionCandidate(BaseModel) |
| PromotionRule | class | class PromotionRule(BaseModel) |
| _MODEL_CONFIG | variable | _MODEL_CONFIG = ConfigDict(extra='forbid', frozen=True) |
| _MODEL_CONFIG | variable | _MODEL_CONFIG = ConfigDict(extra='forbid', frozen=True) |
| _RESOLUTION_VERDICT | variable | _RESOLUTION_VERDICT: dict[Resolution, Verdict] = ... |
| __all__ | variable | __all__ = ['Exemplar', 'rank_similar', 'FEATURE_WEIGHTS'] |
| __all__ | variable | __all__ = ... |
| _neg_iso | function | def _neg_iso(value: str) -> tuple[int, ...] |
| _score | function | def _score(target: ReviewRecord, candidate: ReviewRecord) -> float |
| detect_promotions | function | def detect_promotions(records: list[ReviewRecord], resolutions: list[ResolutionRecord], *, min_count: int = 3) -> list[PromotionCandidate] |
| rank_similar | function | def rank_similar(target: ReviewRecord, records: list[ReviewRecord], resolutions: list[ResolutionRecord], *, top_n: int = 3) -> list[Exemplar] |
| rule_for | function | def rule_for(drift: Drift, rules: tuple[PromotionRule, ...]) -> PromotionRule \| None |
| rule_from_candidate | function | def rule_from_candidate(candidate: PromotionCandidate) -> PromotionRule |
<!-- CDM:END symbols -->
