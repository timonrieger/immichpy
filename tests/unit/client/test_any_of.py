from immichpy.client.generated.models import AssetEditsCreateDto

EDITS = {"edits": [{"action": "rotate", "parameters": {"angle": 90}}]}


def test_any_of_round_trips_through_pydantic() -> None:
    """The CLI validates bodies with model_validate and prints responses with model_dump."""
    dto = AssetEditsCreateDto.model_validate(EDITS)

    assert dto.to_dict()["edits"][0]["parameters"] == {"angle": 90}
    assert dto.model_dump(mode="json")["edits"][0]["parameters"] == {"angle": 90}
