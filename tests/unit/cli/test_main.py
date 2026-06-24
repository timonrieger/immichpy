"""Tests for immichpy.cli.main module."""

from __future__ import annotations

from typer.main import get_command

from immichpy.cli.consts import SKIP_CLIENT_SETUP_KEY
from immichpy.cli.main import app


def skip_for(args: list[str]) -> bool:
    """Resolve the skip-client-setup flag for a given argument list."""
    ctx = get_command(app).make_context("immichpy", args)
    return ctx.meta[SKIP_CLIENT_SETUP_KEY]


class TestSkipClientSetup:
    """Tests for ClientSetupGroup._skip_client_setup branches."""

    def test_help_flag_skips(self) -> None:
        """A help flag at any level skips client setup."""
        assert skip_for(["server", "-h"]) is True
        assert skip_for(["server", "set-server-license", "--help"]) is True

    def test_non_api_command_skips(self) -> None:
        """Top-level config/setup commands never need a client."""
        assert skip_for(["config"]) is True
        assert skip_for(["setup"]) is True

    def test_group_without_leaf_skips(self) -> None:
        """A group invoked without a leaf shows help, so client setup is skipped."""
        assert skip_for(["server"]) is True

    def test_unknown_command_skips(self) -> None:
        """An unknown command errors and needs no client."""
        assert skip_for(["server", "bogus"]) is True

    def test_leaf_command_does_not_skip(self) -> None:
        """A leaf command runs and requires a client."""
        assert skip_for(["server", "get-about-info"]) is False

    def test_leaf_command_with_options_does_not_skip(self) -> None:
        """A leaf command with trailing option tokens still requires a client."""
        assert skip_for(["server", "set-server-license", "--license-key", "X"]) is False
