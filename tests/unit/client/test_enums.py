from immichpy.client.generated.models.asset_bulk_update_dto import AssetBulkUpdateDto
from immichpy.client.generated.models.asset_visibility import AssetVisibility


def test_enum_accepts_unknown_value():
    dto = AssetBulkUpdateDto.from_dict(
        {"ids": [], "visibility": "not-a-known-visibility"}
    )

    assert dto is not None
    assert isinstance(dto.visibility, AssetVisibility)
    assert dto.visibility.value == "not-a-known-visibility"
    assert dto.to_dict()["visibility"] == "not-a-known-visibility"
    assert AssetVisibility("timeline") is AssetVisibility.TIMELINE
