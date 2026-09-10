"""Generated CLI commands for Cluster groups tag (auto-generated, do not edit)."""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import typer

if TYPE_CHECKING:
    from immichpy import AsyncClient

from immichpy.cli.runtime import print_response, run_command, set_nested
from immichpy.client.generated.models import ClusterGroupRequestCreateDto

app = typer.Typer(
    help="""A cluster group is a set of users whose faces are clustered together, so that a person can be shared between them.\n\n[link=https://api.immich.app/endpoints/cluster-groups]Immich API documentation[/link]"""
)


@app.command(
    "accept-cluster-group-request", deprecated=False, rich_help_panel="API commands"
)
def accept_cluster_group_request(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Accept a cluster group request

    [link=https://api.immich.app/endpoints/cluster-groups/acceptClusterGroupRequest]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(
        client.cluster_groups.accept_cluster_group_request, ctx=ctx, **kwargs
    )
    print_response(result, ctx=ctx)


@app.command(
    "cluster-group-regenerate-people", deprecated=False, rich_help_panel="API commands"
)
def cluster_group_regenerate_people(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Regenerate people of users in cluster group

    [link=https://api.immich.app/endpoints/cluster-groups/clusterGroupRegeneratePeople]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(
        client.cluster_groups.cluster_group_regenerate_people, ctx=ctx, **kwargs
    )
    print_response(result, ctx=ctx)


@app.command(
    "create-cluster-group-request", deprecated=False, rich_help_panel="API commands"
)
def create_cluster_group_request(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    user_id: UUID = typer.Option(
        ..., "--user-id", help=r"""User to invite into the cluster group"""
    ),
) -> None:
    """Create a cluster group request

    [link=https://api.immich.app/endpoints/cluster-groups/createClusterGroupRequest]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["user_id"], user_id)
    cluster_group_request_create_dto = ClusterGroupRequestCreateDto.model_validate(
        json_data
    )
    kwargs["cluster_group_request_create_dto"] = cluster_group_request_create_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(
        client.cluster_groups.create_cluster_group_request, ctx=ctx, **kwargs
    )
    print_response(result, ctx=ctx)


@app.command(
    "delete-cluster-group-request", deprecated=False, rich_help_panel="API commands"
)
def delete_cluster_group_request(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Decline a cluster group request

    [link=https://api.immich.app/endpoints/cluster-groups/deleteClusterGroupRequest]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(
        client.cluster_groups.delete_cluster_group_request, ctx=ctx, **kwargs
    )
    print_response(result, ctx=ctx)


@app.command(
    "get-cluster-group-requests", deprecated=False, rich_help_panel="API commands"
)
def get_cluster_group_requests(
    ctx: typer.Context,
) -> None:
    """Retrieve cluster group requests

    [link=https://api.immich.app/endpoints/cluster-groups/getClusterGroupRequests]Immich API documentation[/link]
    """
    kwargs = {}
    client: AsyncClient = ctx.obj["client"]
    result = run_command(
        client.cluster_groups.get_cluster_group_requests, ctx=ctx, **kwargs
    )
    print_response(result, ctx=ctx)


@app.command(
    "get-cluster-group-requests-for-group",
    deprecated=False,
    rich_help_panel="API commands",
)
def get_cluster_group_requests_for_group(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Retrieve the requests sent by a cluster group

    [link=https://api.immich.app/endpoints/cluster-groups/getClusterGroupRequestsForGroup]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(
        client.cluster_groups.get_cluster_group_requests_for_group, ctx=ctx, **kwargs
    )
    print_response(result, ctx=ctx)


@app.command(
    "get-cluster-group-users", deprecated=False, rich_help_panel="API commands"
)
def get_cluster_group_users(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Retrieve the users of a cluster group

    [link=https://api.immich.app/endpoints/cluster-groups/getClusterGroupUsers]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(
        client.cluster_groups.get_cluster_group_users, ctx=ctx, **kwargs
    )
    print_response(result, ctx=ctx)


@app.command("leave-cluster-group", deprecated=False, rich_help_panel="API commands")
def leave_cluster_group(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Leave a cluster group

    [link=https://api.immich.app/endpoints/cluster-groups/leaveClusterGroup]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.cluster_groups.leave_cluster_group, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)
