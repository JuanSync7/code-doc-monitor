"""Render a human-readable status report for a :class:`~taskflow.core.model.TaskGraph`.

The report is a plain-text table summarizing each task and a final tally per
:class:`~taskflow.core.model.Status`. It is read-only with respect to the graph
and deterministic: the same graph always renders the same text.
"""

from __future__ import annotations

from collections import Counter

from ..core.model import Status, TaskGraph

#: Order statuses appear in the report's summary line.
_STATUS_ORDER: tuple[Status, ...] = (
    Status.DONE,
    Status.RUNNING,
    Status.PENDING,
    Status.FAILED,
)


def _tally(graph: TaskGraph) -> Counter[Status]:
    """Count tasks by :class:`Status` across the whole graph."""
    return Counter(task.status for task in graph.tasks.values())


def render_report(graph: TaskGraph) -> str:
    """Return a plain-text report of every task and a per-status summary.

    The body lists one row per task (``id``, ``name``, ``status`` value) in
    insertion order; the trailing summary line counts tasks per status in the
    canonical :data:`_STATUS_ORDER`.
    """
    lines = ["id    name                 status"]
    lines.append("----  -------------------  --------")
    for task in graph.tasks.values():
        lines.append(f"{task.id:<4}  {task.name:<19}  {task.status.value}")
    tally = _tally(graph)
    summary = "  ".join(
        f"{status.value}={tally.get(status, 0)}" for status in _STATUS_ORDER
    )
    lines.append("")
    lines.append(f"summary: {summary}")
    return "\n".join(lines) + "\n"
