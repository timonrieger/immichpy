"""Generated CLI commands for People tag (auto-generated, do not edit)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal
from uuid import UUID

import typer

if TYPE_CHECKING:
    from immichpy import AsyncClient

from immichpy.cli.runtime import (
    parse_json_options,
    print_response,
    run_command,
    set_nested,
)
from immichpy.client.generated.models import (
    AssetFaceUpdateDto,
    MergePersonDto,
    PeopleDeleteDto,
    PeopleUpdateDto,
    PeopleUsersUpsertDto,
    PeopleUsersUpsertType,
    PersonCreateDto,
    PersonDeleteDto,
    PersonUpdateDto,
    PersonUserRole,
    PersonUsersDeleteDtoInner,
    SharingDirection,
)

app = typer.Typer(
    help="""A person is a collection of faces, which can be favorited and named. A person can also be merged into another person. People are automatically created via the face recognition job.\n\n[link=https://api.immich.app/endpoints/people]Immich API documentation[/link]"""
)


@app.command("create-person", deprecated=False, rich_help_panel="API commands")
def create_person(
    ctx: typer.Context,
    birth_date: str | None = typer.Option(
        None, "--birth-date", help=r"""Person date of birth"""
    ),
    color: str | None = typer.Option(None, "--color", help=r"""Person color (hex)"""),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=r"""Mark as favorite"""
    ),
    is_hidden: Literal["true", "false"] | None = typer.Option(
        None, "--is-hidden", help=r"""Person visibility (hidden)"""
    ),
    name: str | None = typer.Option(None, "--name", help=r"""Person name"""),
) -> None:
    """Create a person

    [link=https://api.immich.app/endpoints/people/createPerson]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if birth_date is not None:
        set_nested(json_data, ["birth_date"], birth_date)
    if color is not None:
        set_nested(json_data, ["color"], color)
    if is_favorite is not None:
        set_nested(json_data, ["is_favorite"], is_favorite.lower() == "true")
    if is_hidden is not None:
        set_nested(json_data, ["is_hidden"], is_hidden.lower() == "true")
    if name is not None:
        set_nested(json_data, ["name"], name)
    person_create_dto = PersonCreateDto.model_validate(json_data)
    kwargs["person_create_dto"] = person_create_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.create_person, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("delete-people", deprecated=False, rich_help_panel="API commands")
def delete_people(
    ctx: typer.Context,
    ids: list[UUID] = typer.Option(..., "--ids", help=r"""IDs to process"""),
    user_id: str | None = typer.Option(None, "--user-id", help=r""""""),
) -> None:
    """Delete people

    [link=https://api.immich.app/endpoints/people/deletePeople]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["ids"], ids)
    if user_id is not None:
        set_nested(json_data, ["user_id"], user_id)
    people_delete_dto = PeopleDeleteDto.model_validate(json_data)
    kwargs["people_delete_dto"] = people_delete_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.delete_people, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("delete-person", deprecated=False, rich_help_panel="API commands")
def delete_person(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    user_id: str | None = typer.Option(None, "--user-id", help=r""""""),
) -> None:
    """Delete person

    [link=https://api.immich.app/endpoints/people/deletePerson]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if user_id is not None:
        set_nested(json_data, ["user_id"], user_id)
    person_delete_dto = PersonDeleteDto.model_validate(json_data)
    kwargs["person_delete_dto"] = person_delete_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.delete_person, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-all-people", deprecated=False, rich_help_panel="API commands")
def get_all_people(
    ctx: typer.Context,
    closest_asset_id: UUID | None = typer.Option(
        None, "--closest-asset-id", help=r"""Closest asset ID for similarity search"""
    ),
    closest_person_id: UUID | None = typer.Option(
        None, "--closest-person-id", help=r"""Closest person ID for similarity search"""
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=r"""Filter by favorite status"""
    ),
    is_hidden: Literal["true", "false"] | None = typer.Option(
        None, "--is-hidden", help=r"""Filter by hidden status"""
    ),
    name: str | None = typer.Option(None, "--name", help=r"""Filter by person name"""),
    page: int | None = typer.Option(
        None,
        "--page",
        help=r"""Page number for pagination""",
        min=1,
        max=9007199254740991,
    ),
    shared_by_id: UUID | None = typer.Option(
        None,
        "--shared-by-id",
        help=r"""Only include people to which the user gave access""",
    ),
    shared_with_id: UUID | None = typer.Option(
        None,
        "--shared-with-id",
        help=r"""Only include people to which the user was given access""",
    ),
    size: int | None = typer.Option(
        None, "--size", help=r"""Number of items per page""", min=1, max=1000
    ),
    with_hidden: Literal["true", "false"] | None = typer.Option(
        None, "--with-hidden", help=r"""Include hidden people"""
    ),
) -> None:
    """Get all people

    [link=https://api.immich.app/endpoints/people/getAllPeople]Immich API documentation[/link]
    """
    kwargs = {}
    if closest_asset_id is not None:
        kwargs["closest_asset_id"] = closest_asset_id
    if closest_person_id is not None:
        kwargs["closest_person_id"] = closest_person_id
    if is_favorite is not None:
        kwargs["is_favorite"] = is_favorite.lower() == "true"
    if is_hidden is not None:
        kwargs["is_hidden"] = is_hidden.lower() == "true"
    if name is not None:
        kwargs["name"] = name
    if page is not None:
        kwargs["page"] = page
    if shared_by_id is not None:
        kwargs["shared_by_id"] = shared_by_id
    if shared_with_id is not None:
        kwargs["shared_with_id"] = shared_with_id
    if size is not None:
        kwargs["size"] = size
    if with_hidden is not None:
        kwargs["with_hidden"] = with_hidden.lower() == "true"
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.get_all_people, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-person", deprecated=False, rich_help_panel="API commands")
def get_person(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Get a person

    [link=https://api.immich.app/endpoints/people/getPerson]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.get_person, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-person-statistics", deprecated=False, rich_help_panel="API commands")
def get_person_statistics(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Get person statistics

    [link=https://api.immich.app/endpoints/people/getPersonStatistics]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.get_person_statistics, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-person-thumbnail", deprecated=False, rich_help_panel="API commands")
def get_person_thumbnail(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
) -> None:
    """Get person thumbnail

    [link=https://api.immich.app/endpoints/people/getPersonThumbnail]Immich API documentation[/link]
    """
    kwargs = {}
    kwargs["id"] = id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.get_person_thumbnail, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("get-users-for-people", deprecated=False, rich_help_panel="API commands")
def get_users_for_people(
    ctx: typer.Context,
    direction: SharingDirection | None = typer.Option(
        None, "--direction", help=r""""""
    ),
    person_id: UUID | None = typer.Option(None, "--person-id", help=r"""Person ID"""),
    role: PersonUserRole | None = typer.Option(
        None, "--role", help=r"""Role of user"""
    ),
    shared_by_id: UUID | None = typer.Option(
        None, "--shared-by-id", help=r"""User ID of the user that gave access"""
    ),
    shared_with_id: UUID | None = typer.Option(
        None, "--shared-with-id", help=r"""User ID of the user that was given access"""
    ),
) -> None:
    """Get people access

    [link=https://api.immich.app/endpoints/people/getUsersForPeople]Immich API documentation[/link]
    """
    kwargs = {}
    if direction is not None:
        kwargs["direction"] = direction
    if person_id is not None:
        kwargs["person_id"] = person_id
    if role is not None:
        kwargs["role"] = role
    if shared_by_id is not None:
        kwargs["shared_by_id"] = shared_by_id
    if shared_with_id is not None:
        kwargs["shared_with_id"] = shared_with_id
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.get_users_for_people, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("merge-people", deprecated=False, rich_help_panel="API commands")
def merge_people(
    ctx: typer.Context,
    ids: list[UUID] = typer.Option(..., "--ids", help=r"""Person IDs to merge"""),
) -> None:
    """Merge people

    [link=https://api.immich.app/endpoints/people/mergePeople]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    set_nested(json_data, ["ids"], ids)
    merge_person_dto = MergePersonDto.model_validate(json_data)
    kwargs["merge_person_dto"] = merge_person_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.merge_people, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("merge-person-legacy", deprecated=True, rich_help_panel="API commands")
def merge_person_legacy(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    ids: list[UUID] = typer.Option(..., "--ids", help=r"""Person IDs to merge"""),
) -> None:
    """Merge people

    [link=https://api.immich.app/endpoints/people/mergePersonLegacy]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    set_nested(json_data, ["ids"], ids)
    merge_person_dto = MergePersonDto.model_validate(json_data)
    kwargs["merge_person_dto"] = merge_person_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.merge_person_legacy, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("reassign-faces", deprecated=False, rich_help_panel="API commands")
def reassign_faces(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    data: list[str] = typer.Option(
        ...,
        "--data",
        help=r"""Face update items

As a JSON string with keys: assetId (string), personId (string), userId (string)""",
    ),
) -> None:
    """Reassign faces

    [link=https://api.immich.app/endpoints/people/reassignFaces]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    value_data = parse_json_options(data, "--data", ctx=ctx)
    set_nested(json_data, ["data"], value_data)
    asset_face_update_dto = AssetFaceUpdateDto.model_validate(json_data)
    kwargs["asset_face_update_dto"] = asset_face_update_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.reassign_faces, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command(
    "remove-users-from-people", deprecated=False, rich_help_panel="API commands"
)
def remove_users_from_people(
    ctx: typer.Context,
    items: list[str] = typer.Option(
        ...,
        "--items",
        help=r"""As a JSON string with keys: personId (string), sharedById (string), sharedWithId (string)""",
    ),
) -> None:
    """Remove users from people

    [link=https://api.immich.app/endpoints/people/removeUsersFromPeople]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    value_items = parse_json_options(items, "--items", ctx=ctx)
    set_nested(json_data, ["items"], value_items)
    person_users_delete_dto_inner = [
        PersonUsersDeleteDtoInner.model_validate(item) for item in json_data["items"]
    ]
    kwargs["person_users_delete_dto_inner"] = person_users_delete_dto_inner
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.remove_users_from_people, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("update-people", deprecated=False, rich_help_panel="API commands")
def update_people(
    ctx: typer.Context,
    people: list[str] = typer.Option(
        ...,
        "--people",
        help=r"""People to update

As a JSON string with keys: birthDate (string), color (string), featureFaceAssetId (string), id (string), isFavorite (boolean), isHidden (boolean), name (string), userId (string)""",
    ),
) -> None:
    """Update people

    [link=https://api.immich.app/endpoints/people/updatePeople]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    value_people = parse_json_options(people, "--people", ctx=ctx)
    set_nested(json_data, ["people"], value_people)
    people_update_dto = PeopleUpdateDto.model_validate(json_data)
    kwargs["people_update_dto"] = people_update_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.update_people, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("update-person", deprecated=True, rich_help_panel="API commands")
def update_person(
    ctx: typer.Context,
    id: UUID = typer.Argument(..., help=r""""""),
    birth_date: str | None = typer.Option(
        None, "--birth-date", help=r"""Person date of birth"""
    ),
    color: str | None = typer.Option(None, "--color", help=r"""Person color (hex)"""),
    feature_face_asset_id: UUID | None = typer.Option(
        None,
        "--feature-face-asset-id",
        help=r"""Asset ID used for feature face thumbnail""",
    ),
    is_favorite: Literal["true", "false"] | None = typer.Option(
        None, "--is-favorite", help=r"""Mark as favorite"""
    ),
    is_hidden: Literal["true", "false"] | None = typer.Option(
        None, "--is-hidden", help=r"""Person visibility (hidden)"""
    ),
    name: str | None = typer.Option(None, "--name", help=r"""Person name"""),
    user_id: UUID | None = typer.Option(
        None,
        "--user-id",
        help=r"""Restrict the update to the person record of this User ID""",
    ),
) -> None:
    """Update person

    [link=https://api.immich.app/endpoints/people/updatePerson]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    kwargs["id"] = id
    if birth_date is not None:
        set_nested(json_data, ["birth_date"], birth_date)
    if color is not None:
        set_nested(json_data, ["color"], color)
    if feature_face_asset_id is not None:
        set_nested(json_data, ["feature_face_asset_id"], feature_face_asset_id)
    if is_favorite is not None:
        set_nested(json_data, ["is_favorite"], is_favorite.lower() == "true")
    if is_hidden is not None:
        set_nested(json_data, ["is_hidden"], is_hidden.lower() == "true")
    if name is not None:
        set_nested(json_data, ["name"], name)
    if user_id is not None:
        set_nested(json_data, ["user_id"], user_id)
    person_update_dto = PersonUpdateDto.model_validate(json_data)
    kwargs["person_update_dto"] = person_update_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.update_person, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)


@app.command("upsert-people-users", deprecated=False, rich_help_panel="API commands")
def upsert_people_users(
    ctx: typer.Context,
    person_ids: list[UUID] | None = typer.Option(
        None, "--person-ids", help=r"""Person IDs, required when type is omitted"""
    ),
    role: PersonUserRole = typer.Option(
        ...,
        "--role",
        help=r"""Levels of access for managing people resources on behalf of another user.""",
    ),
    shared_with_ids: list[UUID] = typer.Option(
        ...,
        "--shared-with-ids",
        help=r"""User IDs that should be given access to the person""",
    ),
    type: PeopleUsersUpsertType | None = typer.Option(
        None, "--type", help=r"""Which people to update when personIds is omitted"""
    ),
) -> None:
    """Upsert user access

    [link=https://api.immich.app/endpoints/people/upsertPeopleUsers]Immich API documentation[/link]
    """
    kwargs = {}
    json_data = {}
    if person_ids is not None:
        set_nested(json_data, ["person_ids"], person_ids)
    set_nested(json_data, ["role"], role)
    set_nested(json_data, ["shared_with_ids"], shared_with_ids)
    if type is not None:
        set_nested(json_data, ["type"], type)
    people_users_upsert_dto = PeopleUsersUpsertDto.model_validate(json_data)
    kwargs["people_users_upsert_dto"] = people_users_upsert_dto
    client: AsyncClient = ctx.obj["client"]
    result = run_command(client.people.upsert_people_users, ctx=ctx, **kwargs)
    print_response(result, ctx=ctx)
