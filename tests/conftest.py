from pathlib import Path

import pytest


@pytest.fixture
def mock_config_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Fixture that patches CONFIG_DIR and CONFIG_FILE to use tmp_path."""
    config_dir = tmp_path / ".immichpy"
    config_file = config_dir / "config.toml"

    monkeypatch.setattr("immichpy.cli.consts.CONFIG_DIR", config_dir)
    monkeypatch.setattr("immichpy.cli.consts.CONFIG_FILE", config_file)
    monkeypatch.setattr("immichpy.cli.utils.CONFIG_FILE", config_file)
    monkeypatch.setattr("immichpy.cli.wrapper.setup.CONFIG_FILE", config_file)
    monkeypatch.setattr("immichpy.cli.wrapper.config.CONFIG_FILE", config_file)

    return config_file
