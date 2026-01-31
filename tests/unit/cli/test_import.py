"""Tests for immichpy.cli.main module import."""

import typer

from immichpy.cli import main


def test_import_main_module() -> None:
    """Test that the main CLI module can be imported and called."""
    assert main is not None
    assert hasattr(main, "app")
    assert main.app is not None
    assert callable(main.app)
    assert isinstance(main.app, typer.Typer)
