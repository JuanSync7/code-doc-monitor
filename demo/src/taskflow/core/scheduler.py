"""Standalone scheduling helpers over a :class:`~taskflow.core.model.TaskGraph`.

This module is intentionally **undocumented** in the demo: it is a public,
behaving source file under the ``core`` unit's ``dir-covered`` that no document
references, so it surfaces in ``coverage.rpt`` as a real coverage gap (its
``suggested_unit`` is ``core``). It is otherwise a normal, working module.
"""

from __future__ import annotations

from .model import TaskGraph


def priority_order(graph: TaskGraph) -> tuple[str, ...]:
    """Return the ids of tasks that are ready to run, sorted by name.

    A task is *ready* when it has no dependencies (a root of ``graph``). Ties on
    name are broken by id so the result is fully deterministic.

    Args:
        graph: The task graph to inspect.

    Returns:
        The ready tasks' ids, ordered by ``(name, id)``.
    """
    ready = [graph.get(tid) for tid in graph.roots()]
    return tuple(task.id for task in sorted(ready, key=lambda t: (t.name, t.id)))
