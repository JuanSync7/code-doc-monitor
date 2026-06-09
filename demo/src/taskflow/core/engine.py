"""The scheduling engine: order a :class:`~taskflow.core.model.TaskGraph` by its
dependencies and run it.

The engine is pure with respect to the graph it is given a reference to: it
mutates task :class:`~taskflow.core.model.Status` as work progresses but creates
no global state. Execution is sequential and deterministic — tasks run in a
stable topological order, so a graph always produces the same run sequence.
"""

from __future__ import annotations

from collections.abc import Callable

from .model import Status, Task, TaskGraph

#: A task runner: given a :class:`Task`, return ``True`` on success.
Runner = Callable[[Task], bool]


class CycleError(ValueError):
    """Raised when a :class:`TaskGraph` contains a dependency cycle.

    Carries the ids still unresolved when the topological sort stalled, so a
    caller can report exactly which tasks form the cycle.
    """

    def __init__(self, unresolved: tuple[str, ...]) -> None:
        self.unresolved = unresolved
        super().__init__(f"dependency cycle among tasks: {sorted(unresolved)}")


class Engine:
    """Order and run the tasks of a :class:`TaskGraph`.

    The engine holds a reference to the graph and never copies it; running the
    engine updates the tasks' statuses in place.
    """

    def __init__(self, graph: TaskGraph) -> None:
        self.graph = graph

    def topological_order(self) -> tuple[str, ...]:
        """Return task ids in a stable dependency-respecting order.

        Uses Kahn's algorithm over the graph's edges, breaking ties by insertion
        order so the result is deterministic.

        Raises:
            CycleError: if the graph contains a dependency cycle.
        """
        indegree = {tid: len(t.deps) for tid, t in self.graph.tasks.items()}
        ready = [tid for tid in self.graph.tasks if indegree[tid] == 0]
        order: list[str] = []
        while ready:
            current = ready.pop(0)
            order.append(current)
            for succ in self.graph.successors(current):
                indegree[succ] -= 1
                if indegree[succ] == 0:
                    ready.append(succ)
        if len(order) != len(self.graph.tasks):
            unresolved = tuple(tid for tid, deg in indegree.items() if deg > 0)
            raise CycleError(unresolved)
        return tuple(order)

    def run(self, runner: Runner) -> tuple[str, ...]:
        """Run every task in dependency order, calling ``runner`` on each.

        A task is marked :attr:`Status.RUNNING` before ``runner`` is invoked and
        then :attr:`Status.DONE` or :attr:`Status.FAILED` by its result. When a
        task fails, every task that (transitively) depends on it is skipped and
        marked :attr:`Status.FAILED` without being run.

        Returns:
            The ids of tasks that completed successfully, in run order.
        """
        completed: list[str] = []
        failed: set[str] = set()
        for tid in self.topological_order():
            task = self.graph.get(tid)
            if any(dep in failed for dep in task.deps):
                task.status = Status.FAILED
                failed.add(tid)
                continue
            task.status = Status.RUNNING
            if runner(task):
                task.status = Status.DONE
                completed.append(tid)
            else:
                task.status = Status.FAILED
                failed.add(tid)
        return tuple(completed)
