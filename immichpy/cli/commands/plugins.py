"""Generated CLI commands for Plugins tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from uuid import UUID
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immichpy import AsyncClient

from immichpy.cli.runtime import print_response, run_command
from immichpy.client.generated.models import *

app = typer.Typer(
    help="""A plugin is an installed module that makes filters and actions available for the workflow feature.\n\n[link=https://api.immich.app/endpoints/plugins]Immich API documentation[/link]"""
)


@app.command("get-plugin", deprecated=False, rich_help_panel="API commands")
def get_plugin(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=""""""),
) -> None:
    """Retrieve a plugin

    [link=https://api.immich.app/endpoints/plugins/getPlugin]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.plugins.get_plugin, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("search-plugin-methods", deprecated=False, rich_help_panel="API commands")
def search_plugin_methods(
    ctx: typer.Context,
    description: str | None = typer.Option(None, "--description", help=""""""),
    enabled: Literal["true", "false"] | None = typer.Option(
        None, "--enabled", help="""Whether the plugin method is enabled"""
    ),
    id: UUID | None = typer.Option(None, "--id", help="""Plugin method ID"""),
    name: str | None = typer.Option(None, "--name", help=""""""),
    plugin_name: str | None = typer.Option(
        None, "--plugin-name", help="""Plugin name"""
    ),
    plugin_version: str | None = typer.Option(
        None, "--plugin-version", help="""Plugin version"""
    ),
    title: str | None = typer.Option(None, "--title", help=""""""),
    trigger: WorkflowTrigger | None = typer.Option(
        None, "--trigger", help="""Workflow trigger"""
    ),
    type: WorkflowType | None = typer.Option(None, "--type", help="""Workflow types"""),
) -> None:
    """Retrieve plugin methods

    [link=https://api.immich.app/endpoints/plugins/searchPluginMethods]Immich API documentation[/link]
    """
    kwargs = {}
    if description is not None:
        kwargs["description"] = description
    if enabled is not None:
        kwargs["enabled"] = enabled.lower() == "true"
    if id is not None:
        kwargs["id"] = id
    if name is not None:
        kwargs["name"] = name
    if plugin_name is not None:
        kwargs["plugin_name"] = plugin_name
    if plugin_version is not None:
        kwargs["plugin_version"] = plugin_version
    if title is not None:
        kwargs["title"] = title
    if trigger is not None:
        kwargs["trigger"] = trigger
    if type is not None:
        kwargs["type"] = type
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.plugins.search_plugin_methods, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command(
    "search-plugin-templates", deprecated=False, rich_help_panel="API commands"
)
def search_plugin_templates(
    ctx: typer.Context,
) -> None:
    """Retrieve workflow templates

    [link=https://api.immich.app/endpoints/plugins/searchPluginTemplates]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.plugins.search_plugin_templates, ctx=ctx, **kwargs)
    print_response(result, ctx)


@app.command("search-plugins", deprecated=False, rich_help_panel="API commands")
def search_plugins(
    ctx: typer.Context,
    description: str | None = typer.Option(None, "--description", help=""""""),
    enabled: Literal["true", "false"] | None = typer.Option(
        None, "--enabled", help="""Whether the plugin is enabled"""
    ),
    id: UUID | None = typer.Option(None, "--id", help="""Plugin ID"""),
    name: str | None = typer.Option(None, "--name", help=""""""),
    title: str | None = typer.Option(None, "--title", help=""""""),
    version: str | None = typer.Option(None, "--version", help=""""""),
) -> None:
    """List all plugins

    [link=https://api.immich.app/endpoints/plugins/searchPlugins]Immich API documentation[/link]
    """
    kwargs = {}
    if description is not None:
        kwargs["description"] = description
    if enabled is not None:
        kwargs["enabled"] = enabled.lower() == "true"
    if id is not None:
        kwargs["id"] = id
    if name is not None:
        kwargs["name"] = name
    if title is not None:
        kwargs["title"] = title
    if version is not None:
        kwargs["version"] = version
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.plugins.search_plugins, ctx=ctx, **kwargs)
    print_response(result, ctx)
