"""Generated CLI commands for Config (public) tag (auto-generated, do not edit)."""

from __future__ import annotations

from typing import TYPE_CHECKING

import typer

if TYPE_CHECKING:
    from immichpy import AsyncClient

from immichpy.cli.runtime import print_response, run_command
from immichpy.client.generated.models import *

app = typer.Typer(
    help="""The system configuration properties that are visible to everyone.\n\n[link=https://api.immich.app/endpoints/config-public]Immich API documentation[/link]"""
)


@app.command("get-public-config", deprecated=False, rich_help_panel="API commands")
def get_public_config(
    ctx: typer.Context,
) -> None:
    """Get the public configuration

    [link=https://api.immich.app/endpoints/config-public/getPublicConfig]Immich API documentation[/link]
    """
    kwargs = {}
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.config_public.get_public_config, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command(
    "get-public-config-defaults", deprecated=False, rich_help_panel="API commands"
)
def get_public_config_defaults(
    ctx: typer.Context,
) -> None:
    """Get the public configuration defaults

    [link=https://api.immich.app/endpoints/config-public/getPublicConfigDefaults]Immich API documentation[/link]
    """
    kwargs = {}
    client: AsyncClient = ctx.obj["client"]
    result = run_command(
        client.config_public.get_public_config_defaults, ctx=ctx, **kwargs
    )
    print_response(result, ctx=ctx)
