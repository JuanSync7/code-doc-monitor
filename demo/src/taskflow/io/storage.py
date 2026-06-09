"""Persist and load a :class:`~taskflow.core.model.TaskGraph` as JSON.

The on-disk format is a single JSON object with a ``tasks`` list; each task is
serialized with its ``id``, ``name``, ``deps``, and ``status`` string token.
Loading is the exact inverse of saving, so ``load_graph(save_graph(g))``
reproduces ``g``.
"""

from __future__ import annotations

import json
from pathlib import Path

from ..core.model import Status, Task, TaskGraph


def _task_to_dict(task: Task) -> dict[str, object]:
    """Project a :class:`Task` onto a JSON-serializable mapping."""
    return {
        "id": task.id,
        "name": task.name,
        "deps": list(task.deps),
        "status": task.status.value,
    }


def _task_from_dict(data: dict[str, object]) -> Task:
    """Rebuild a :class:`Task` from a mapping produced by :func:`_task_to_dict`."""
    raw_deps = data.get("deps", [])
    deps = tuple(str(d) for d in raw_deps) if isinstance(raw_deps, list) else ()
    return Task(
        id=str(data["id"]),
        name=str(data["name"]),
        deps=deps,
        status=Status(str(data.get("status", Status.PENDING.value))),
    )


def save_graph(graph: TaskGraph, path: Path) -> None:
    """Write ``graph`` to ``path`` as formatted JSON (UTF-8).

    Tasks are written in their insertion order so the file is stable across
    repeated saves of an unchanged graph.
    """
    payload = {"tasks": [_task_to_dict(t) for t in graph.tasks.values()]}
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def load_graph(path: Path) -> TaskGraph:
    """Read a :class:`TaskGraph` back from a JSON file written by :func:`save_graph`.

    Raises:
        ValueError: if the file's top level is not a JSON object with a
            list-valued ``tasks`` key.
    """
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or not isinstance(raw.get("tasks"), list):
        raise ValueError(f"{path}: expected an object with a 'tasks' list")
    graph = TaskGraph()
    for entry in raw["tasks"]:
        graph.add(_task_from_dict(entry))
    return graph
