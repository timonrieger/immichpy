"""Generated CLI commands for Passkeys tag (auto-generated, do not edit)."""

from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID

import typer

if TYPE_CHECKING:
    from immichpy import AsyncClient

from immichpy.cli.runtime import print_response, run_command, set_nested
from immichpy.client.generated.models import (
    PasskeyAuthenticationFinishDto,
    PasskeyRegistrationFinishDto,
    PasskeyUpdateDto,
)

app = typer.Typer(
    help="""A passkey is a WebAuthn credential that can be used to login without a password.\n\n[link=https://api.immich.app/endpoints/passkeys]Immich API documentation[/link]"""
)


@app.command("delete-passkey", deprecated=False, rich_help_panel="API commands")
def delete_passkey(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Delete a passkey

    [link=https://api.immich.app/endpoints/passkeys/deletePasskey]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.passkeys.delete_passkey, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("finish-authentication", deprecated=False, rich_help_panel="API commands")
def finish_authentication(
    ctx: typer.Context,
    response_id: str = typer.Option(..., "--response-id", help=r"""Credential ID"""),
    response_response_user_handle: str | None = typer.Option(
        None, "--response-response-user-handle", help=r"""User handle"""
    ),
) -> None:
    """Finish passkey authentication

    [link=https://api.immich.app/endpoints/passkeys/finishAuthentication]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["response", "id"], response_id)
    if response_response_user_handle is not None:
        set_nested(
            json_data,
            ["response", "response", "userHandle"],
            response_response_user_handle,
        )
    passkey_authentication_finish_dto = PasskeyAuthenticationFinishDto.model_validate(
        json_data
    )
    kwargs["passkey_authentication_finish_dto"] = passkey_authentication_finish_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.passkeys.finish_authentication, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("finish-registration", deprecated=False, rich_help_panel="API commands")
def finish_registration(
    ctx: typer.Context,
    name: str | None = typer.Option(None, "--name", help=r"""Passkey name"""),
) -> None:
    """Finish passkey registration

    [link=https://api.immich.app/endpoints/passkeys/finishRegistration]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if name is not None:
        set_nested(json_data, ["name"], name)
    passkey_registration_finish_dto = PasskeyRegistrationFinishDto.model_validate(
        json_data
    )
    kwargs["passkey_registration_finish_dto"] = passkey_registration_finish_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.passkeys.finish_registration, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-passkey", deprecated=False, rich_help_panel="API commands")
def get_passkey(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Retrieve a passkey

    [link=https://api.immich.app/endpoints/passkeys/getPasskey]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.passkeys.get_passkey, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("search-passkeys", deprecated=False, rich_help_panel="API commands")
def search_passkeys(
    ctx: typer.Context,
    id: UUID | None = typer.Option(None, "--id", help=r"""Filter by passkey ID"""),
) -> None:
    """Search passkeys

    [link=https://api.immich.app/endpoints/passkeys/searchPasskeys]Immich API documentation[/link]
    """
    kwargs = {}
    if id is not None:
        kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.passkeys.search_passkeys, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("start-authentication", deprecated=False, rich_help_panel="API commands")
def start_authentication(
    ctx: typer.Context,
) -> None:
    """Start passkey authentication

    [link=https://api.immich.app/endpoints/passkeys/startAuthentication]Immich API documentation[/link]
    """
    kwargs = {}
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.passkeys.start_authentication, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("start-registration", deprecated=False, rich_help_panel="API commands")
def start_registration(
    ctx: typer.Context,
) -> None:
    """Start passkey registration

    [link=https://api.immich.app/endpoints/passkeys/startRegistration]Immich API documentation[/link]
    """
    kwargs = {}
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.passkeys.start_registration, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("update-passkey", deprecated=False, rich_help_panel="API commands")
def update_passkey(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    name: str = typer.Option(..., "--name", help=r"""Passkey name"""),
) -> None:
    """Update a passkey

    [link=https://api.immich.app/endpoints/passkeys/updatePasskey]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["name"], name)
    passkey_update_dto = PasskeyUpdateDto.model_validate(json_data)
    kwargs["passkey_update_dto"] = passkey_update_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.passkeys.update_passkey, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)
