"""Generated CLI commands for Workflows tag (auto-generated, do not edit)."""

from __future__ import annotations

import typer
from uuid import UUID
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from immichpy import AsyncClient

from immichpy.cli.runtime import (
    parse_json_options,
    print_response,
    run_command,
    set_nested,
)
from immichpy.client.generated.models import *

app = typer.Typer(
    help="""A workflow is a set of actions that run whenever a triggering event occurs. Workflows also can include filters to further limit execution.\n\n[link=https://api.immich.app/endpoints/workflows]Immich API documentation[/link]"""
)


@app.command("create-workflow", deprecated=False, rich_help_panel="API commands")
def create_workflow(
    ctx: typer.Context,
    description: str | None = typer.Option(
        None, "--description", help=r"""Workflow description"""
    ),
    enabled: Literal["true", "false"] | None = typer.Option(
        None, "--enabled", help=r"""Workflow enabled"""
    ),
    name: str | None = typer.Option(None, "--name", help=r"""Workflow name"""),
    steps: list[str] | None = typer.Option(
        None,
        "--steps",
        help=r"""As a JSON string with keys: config (object), enabled (boolean), method (string)""",
    ),
    trigger: str = typer.Option(..., "--trigger", help=r"""Plugin trigger type"""),
) -> None:
    """Create a workflow

    [link=https://api.immich.app/endpoints/workflows/createWorkflow]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if description is not None:
        set_nested(json_data, ["description"], description)
    if enabled is not None:
        set_nested(json_data, ["enabled"], enabled.lower() == "true")
    if name is not None:
        set_nested(json_data, ["name"], name)
    if steps is not None:
        value_steps = parse_json_options(steps, "--steps", ctx=ctx)
        set_nested(json_data, ["steps"], value_steps)
    set_nested(json_data, ["trigger"], trigger)
    workflow_create_dto = WorkflowCreateDto.model_validate(json_data)
    kwargs["workflow_create_dto"] = workflow_create_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.workflows.create_workflow, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("delete-workflow", deprecated=False, rich_help_panel="API commands")
def delete_workflow(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Delete a workflow

    [link=https://api.immich.app/endpoints/workflows/deleteWorkflow]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.workflows.delete_workflow, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-workflow", deprecated=False, rich_help_panel="API commands")
def get_workflow(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Retrieve a workflow

    [link=https://api.immich.app/endpoints/workflows/getWorkflow]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.workflows.get_workflow, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-workflow-for-share", deprecated=False, rich_help_panel="API commands")
def get_workflow_for_share(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Retrieve a workflow

    [link=https://api.immich.app/endpoints/workflows/getWorkflowForShare]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.workflows.get_workflow_for_share, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-workflow-triggers", deprecated=False, rich_help_panel="API commands")
def get_workflow_triggers(
    ctx: typer.Context,
) -> None:
    """List all workflow triggers

    [link=https://api.immich.app/endpoints/workflows/getWorkflowTriggers]Immich API documentation[/link]
    """
    kwargs = {}
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.workflows.get_workflow_triggers, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("search-workflows", deprecated=False, rich_help_panel="API commands")
def search_workflows(
    ctx: typer.Context,
    description: str | None = typer.Option(
        None, "--description", help=r"""Workflow description"""
    ),
    enabled: Literal["true", "false"] | None = typer.Option(
        None, "--enabled", help=r"""Workflow enabled"""
    ),
    id: UUID | None = typer.Option(None, "--id", help=r"""Workflow ID"""),
    name: str | None = typer.Option(None, "--name", help=r"""Workflow name"""),
    trigger: WorkflowTrigger | None = typer.Option(
        None, "--trigger", help=r"""Workflow trigger type"""
    ),
) -> None:
    """List all workflows

    [link=https://api.immich.app/endpoints/workflows/searchWorkflows]Immich API documentation[/link]
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
    if trigger is not None:
        kwargs["trigger"] = trigger
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.workflows.search_workflows, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("update-workflow", deprecated=True, rich_help_panel="API commands")
def update_workflow(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    description: str | None = typer.Option(
        None, "--description", help=r"""Workflow description"""
    ),
    enabled: Literal["true", "false"] | None = typer.Option(
        None, "--enabled", help=r"""Workflow enabled"""
    ),
    name: str | None = typer.Option(None, "--name", help=r"""Workflow name"""),
    steps: list[str] | None = typer.Option(
        None,
        "--steps",
        help=r"""As a JSON string with keys: config (object), enabled (boolean), method (string)""",
    ),
    trigger: str | None = typer.Option(
        None, "--trigger", help=r"""Plugin trigger type"""
    ),
) -> None:
    """Update a workflow

    [link=https://api.immich.app/endpoints/workflows/updateWorkflow]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if description is not None:
        set_nested(json_data, ["description"], description)
    if enabled is not None:
        set_nested(json_data, ["enabled"], enabled.lower() == "true")
    if name is not None:
        set_nested(json_data, ["name"], name)
    if steps is not None:
        value_steps = parse_json_options(steps, "--steps", ctx=ctx)
        set_nested(json_data, ["steps"], value_steps)
    if trigger is not None:
        set_nested(json_data, ["trigger"], trigger)
    workflow_update_dto = WorkflowUpdateDto.model_validate(json_data)
    kwargs["workflow_update_dto"] = workflow_update_dto
    client: "AsyncClient" = ctx.obj["client"]
    result = run_command(client.workflows.update_workflow, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)
