from datetime import UTC, datetime, timedelta, timezone

import pytest

from immichpy.client.generated.api.map_api import MapApi
from immichpy.client.generated.api_client import ApiClient


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (datetime(2024, 1, 1, tzinfo=UTC), "2024-01-01T00%3A00%3A00%2B00%3A00"),
        (
            datetime(2024, 1, 1, tzinfo=timezone(timedelta(hours=5, minutes=30))),
            "2024-01-01T00%3A00%3A00%2B05%3A30",
        ),
    ],
)
def test_datetime_query_param_is_iso_8601(value: datetime, expected: str) -> None:
    """Datetime query params keep the colon in the offset, which the server requires."""
    api = MapApi(ApiClient())
    _, url, _, _, _ = api._get_map_markers_serialize(
        file_created_after=value,
        file_created_before=None,
        is_archived=None,
        is_favorite=None,
        with_partners=None,
        with_shared_albums=None,
        _request_auth=None,
        _content_type=None,
        _headers=None,
        _host_index=0,
    )

    assert f"fileCreatedAfter={expected}" in url
