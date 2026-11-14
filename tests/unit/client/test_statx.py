from __future__ import annotations

import sys
import time
from pathlib import Path

import pytest

from immichpy.client.utils.statx import birthtime


@pytest.mark.skipif(sys.platform != "linux", reason="statx is Linux-only")
def test_birthtime_of_new_file(tmp_path: Path) -> None:
    path = tmp_path / "file"
    path.touch()
    btime = birthtime(str(path))
    assert btime is not None
    assert abs(btime - time.time()) < 60


def test_birthtime_of_missing_file(tmp_path: Path) -> None:
    assert birthtime(str(tmp_path / "missing")) is None
