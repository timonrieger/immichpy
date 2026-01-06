from __future__ import annotations

from pathlib import Path
from typing import Any, Optional
from uuid import UUID

from immich.client.api.users_api import UsersApi
from immich.utils import resolve_output_filename


class UsersApiWrapped(UsersApi):
    async def get_profile_image_to_file(
        self,
        id: UUID,
        out_dir: Path,
        filename: Optional[str] = None,
        **kwargs: Any,
    ) -> Path:
        """
        Download a user's profile image and save it to a file.

        :param id: The user ID.
        :param out_dir: The directory to write the profile image to.
        :param filename: The filename to use. If not provided, we try to derive it from the headers
            or default to "profile-" + user_id.
        :param kwargs: Additional arguments to pass to the `get_profile_image_with_http_info` method.

        For exact request/response behavior, inspect `UsersApi.get_profile_image_with_http_info`
        in the generated client.
        """
        resp = await super().get_profile_image_with_http_info(id=id, **kwargs)
        name = resolve_output_filename(
            resp.headers,
            name=filename,
            default_base=f"profile-{id}",
        )

        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / name
        out_path.write_bytes(bytes(resp.data))
        return out_path
