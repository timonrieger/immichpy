"""Generated CLI commands for Config (user) tag (auto-generated, do not edit)."""

from __future__ import annotations

from typing import TYPE_CHECKING

import typer

if TYPE_CHECKING:
    from immichpy import AsyncClient

from immichpy.cli.runtime import print_response, run_command

app = typer.Typer(
    help="""The system configuration properties that are visible to logged in users.\n\n[link=https://api.immich.app/endpoints/config-user]Immich API documentation[/link]"""
)


@app.command("get-user-config", deprecated=False, rich_help_panel="API commands")
def get_user_config(
    ctx: typer.Context,
) -> None:
    """Get the configuration with user visibility

    [link=https://api.immich.app/endpoints/config-user/getUserConfig]Immich API documentation[/link]
    """
    kwargs = {}
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.config_user.get_user_config, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command(
    "get-user-config-defaults", deprecated=False, rich_help_panel="API commands"
)
def get_user_config_defaults(
    ctx: typer.Context,
) -> None:
    """Get the default configuration with user visibility

    [link=https://api.immich.app/endpoints/config-user/getUserConfigDefaults]Immich API documentation[/link]
    """
    kwargs = {}
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.config_user.get_user_config_defaults, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)
