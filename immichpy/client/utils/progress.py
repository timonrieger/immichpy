"""Progress bars for uploads and downloads. `rich` is only required when they are shown."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, TypeAlias, cast

if TYPE_CHECKING:
    from rich.progress import Progress, TaskID


class NullProgress:
    """No-op stand-in for `rich.progress.Progress` when no progress is shown."""

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *exc_info: object) -> None:
        pass

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def add_task(self, description: str, total: float | None = None) -> TaskID:
        return cast("TaskID", 0)

    def update(
        self,
        task_id: TaskID,
        *,
        advance: float | None = None,
        completed: float | None = None,
    ) -> None:
        pass


ProgressBar: TypeAlias = "Progress | NullProgress"


def create_progress(show_progress: bool, *, transfer: bool = True) -> ProgressBar:
    """Create a progress bar, or a no-op one if `show_progress` is False.

    :param show_progress: Whether to show the progress bar.
    :param transfer: Whether to add size, speed and remaining time columns.

    :return: A rich `Progress` or a `NullProgress`.
    """
    if not show_progress:
        return NullProgress()
    try:
        from rich.progress import (
            BarColumn,
            DownloadColumn,
            Progress,
            ProgressColumn,
            SpinnerColumn,
            TextColumn,
            TimeRemainingColumn,
            TransferSpeedColumn,
        )
    except ImportError as e:
        raise ImportError(
            'show_progress=True requires rich: pip install "immichpy[cli]"'
        ) from e
    columns: list[ProgressColumn] = [
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ]
    if transfer:
        columns += [DownloadColumn(), TransferSpeedColumn(), TimeRemainingColumn()]
    return Progress(*columns)
