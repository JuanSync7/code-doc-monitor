"""The task domain model: a :class:`Task`, its :class:`Status`, and the
:class:`TaskGraph` that holds tasks and their dependency edges.

The model is deliberately small and pure: it stores data and answers structural
questions (predecessors, successors, roots) but performs no scheduling itself —
that is :mod:`taskflow.core.engine`'s job. Tasks are identified by a unique
string ``id``; a dependency edge ``a -> b`` means "``b`` depends on ``a``", i.e.
``a`` must complete before ``b`` may start.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Status(str, Enum):
    """The lifecycle state of a single task.

    A task starts :attr:`PENDING`, becomes :attr:`RUNNING` while the engine
    works it, then settles into :attr:`DONE` or :attr:`FAILED`. The string
    values are stable on-disk tokens used by :mod:`taskflow.io.storage`.
    """

    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"

    @property
    def is_terminal(self) -> bool:
        """True when the status is final (``DONE`` or ``FAILED``)."""
        return self in (Status.DONE, Status.FAILED)


@dataclass
class Task:
    """One unit of work in a :class:`TaskGraph`.

    Args:
        id: Unique identifier of the task within its graph.
        name: Human-readable label shown in reports.
        deps: Ids of tasks that must complete before this one may start.
        status: Current lifecycle state (defaults to :attr:`Status.PENDING`).
    """

    id: str
    name: str
    deps: tuple[str, ...] = ()
    status: Status = Status.PENDING

    def depends_on(self, task_id: str) -> bool:
        """Return whether this task directly depends on ``task_id``."""
        return task_id in self.deps


@dataclass
class TaskGraph:
    """A directed dependency graph of :class:`Task` objects keyed by id.

    The graph owns the tasks and answers structural queries about them. It does
    not validate acyclicity on insertion; :meth:`taskflow.core.engine.Engine.
    topological_order` is where a cycle surfaces.
    """

    tasks: dict[str, Task] = field(default_factory=dict)

    def add(self, task: Task) -> None:
        """Add ``task`` to the graph.

        Raises:
            KeyError: if a task with the same ``id`` already exists.
        """
        if task.id in self.tasks:
            raise KeyError(f"duplicate task id {task.id!r}")
        self.tasks[task.id] = task

    def get(self, task_id: str) -> Task:
        """Return the task with ``task_id``.

        Raises:
            KeyError: if no such task exists.
        """
        return self.tasks[task_id]

    def predecessors(self, task_id: str) -> tuple[str, ...]:
        """Return the ids of tasks that ``task_id`` directly depends on."""
        return self.tasks[task_id].deps

    def successors(self, task_id: str) -> tuple[str, ...]:
        """Return the ids of tasks that directly depend on ``task_id``."""
        return tuple(other.id for other in self.tasks.values() if task_id in other.deps)

    def roots(self) -> tuple[str, ...]:
        """Return the ids of tasks with no dependencies, in insertion order."""
        return tuple(t.id for t in self.tasks.values() if not t.deps)
