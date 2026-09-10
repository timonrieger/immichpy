# flake8: noqa

# import apis into api package
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from immichpy.client.generated.api.api_keys_api import APIKeysApi
    from immichpy.client.generated.api.activities_api import ActivitiesApi
    from immichpy.client.generated.api.albums_api import AlbumsApi
    from immichpy.client.generated.api.asset_files_api import AssetFilesApi
    from immichpy.client.generated.api.assets_api import AssetsApi
    from immichpy.client.generated.api.authentication_api import AuthenticationApi
    from immichpy.client.generated.api.authentication_admin_api import (
        AuthenticationAdminApi,
    )
    from immichpy.client.generated.api.cluster_groups_api import ClusterGroupsApi
    from immichpy.client.generated.api.config_admin_api import ConfigAdminApi
    from immichpy.client.generated.api.config_public_api import ConfigPublicApi
    from immichpy.client.generated.api.config_user_api import ConfigUserApi
    from immichpy.client.generated.api.database_backups_admin_api import (
        DatabaseBackupsAdminApi,
    )
    from immichpy.client.generated.api.deprecated_api import DeprecatedApi
    from immichpy.client.generated.api.download_api import DownloadApi
    from immichpy.client.generated.api.duplicates_api import DuplicatesApi
    from immichpy.client.generated.api.faces_api import FacesApi
    from immichpy.client.generated.api.jobs_api import JobsApi
    from immichpy.client.generated.api.libraries_api import LibrariesApi
    from immichpy.client.generated.api.maintenance_admin_api import MaintenanceAdminApi
    from immichpy.client.generated.api.map_api import MapApi
    from immichpy.client.generated.api.memories_api import MemoriesApi
    from immichpy.client.generated.api.notifications_api import NotificationsApi
    from immichpy.client.generated.api.notifications_admin_api import (
        NotificationsAdminApi,
    )
    from immichpy.client.generated.api.partners_api import PartnersApi
    from immichpy.client.generated.api.people_api import PeopleApi
    from immichpy.client.generated.api.plugins_api import PluginsApi
    from immichpy.client.generated.api.queues_api import QueuesApi
    from immichpy.client.generated.api.search_api import SearchApi
    from immichpy.client.generated.api.server_api import ServerApi
    from immichpy.client.generated.api.sessions_api import SessionsApi
    from immichpy.client.generated.api.shared_links_api import SharedLinksApi
    from immichpy.client.generated.api.stacks_api import StacksApi
    from immichpy.client.generated.api.sync_api import SyncApi
    from immichpy.client.generated.api.system_config_api import SystemConfigApi
    from immichpy.client.generated.api.system_metadata_api import SystemMetadataApi
    from immichpy.client.generated.api.tags_api import TagsApi
    from immichpy.client.generated.api.timeline_api import TimelineApi
    from immichpy.client.generated.api.trash_api import TrashApi
    from immichpy.client.generated.api.users_api import UsersApi
    from immichpy.client.generated.api.users_admin_api import UsersAdminApi
    from immichpy.client.generated.api.views_api import ViewsApi
    from immichpy.client.generated.api.workflows_api import WorkflowsApi

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "APIKeysApi": ("immichpy.client.generated.api.api_keys_api", "APIKeysApi"),
    "ActivitiesApi": ("immichpy.client.generated.api.activities_api", "ActivitiesApi"),
    "AlbumsApi": ("immichpy.client.generated.api.albums_api", "AlbumsApi"),
    "AssetFilesApi": ("immichpy.client.generated.api.asset_files_api", "AssetFilesApi"),
    "AssetsApi": ("immichpy.client.generated.api.assets_api", "AssetsApi"),
    "AuthenticationAdminApi": (
        "immichpy.client.generated.api.authentication_admin_api",
        "AuthenticationAdminApi",
    ),
    "AuthenticationApi": (
        "immichpy.client.generated.api.authentication_api",
        "AuthenticationApi",
    ),
    "ClusterGroupsApi": (
        "immichpy.client.generated.api.cluster_groups_api",
        "ClusterGroupsApi",
    ),
    "ConfigAdminApi": (
        "immichpy.client.generated.api.config_admin_api",
        "ConfigAdminApi",
    ),
    "ConfigPublicApi": (
        "immichpy.client.generated.api.config_public_api",
        "ConfigPublicApi",
    ),
    "ConfigUserApi": ("immichpy.client.generated.api.config_user_api", "ConfigUserApi"),
    "DatabaseBackupsAdminApi": (
        "immichpy.client.generated.api.database_backups_admin_api",
        "DatabaseBackupsAdminApi",
    ),
    "DeprecatedApi": ("immichpy.client.generated.api.deprecated_api", "DeprecatedApi"),
    "DownloadApi": ("immichpy.client.generated.api.download_api", "DownloadApi"),
    "DuplicatesApi": ("immichpy.client.generated.api.duplicates_api", "DuplicatesApi"),
    "FacesApi": ("immichpy.client.generated.api.faces_api", "FacesApi"),
    "JobsApi": ("immichpy.client.generated.api.jobs_api", "JobsApi"),
    "LibrariesApi": ("immichpy.client.generated.api.libraries_api", "LibrariesApi"),
    "MaintenanceAdminApi": (
        "immichpy.client.generated.api.maintenance_admin_api",
        "MaintenanceAdminApi",
    ),
    "MapApi": ("immichpy.client.generated.api.map_api", "MapApi"),
    "MemoriesApi": ("immichpy.client.generated.api.memories_api", "MemoriesApi"),
    "NotificationsAdminApi": (
        "immichpy.client.generated.api.notifications_admin_api",
        "NotificationsAdminApi",
    ),
    "NotificationsApi": (
        "immichpy.client.generated.api.notifications_api",
        "NotificationsApi",
    ),
    "PartnersApi": ("immichpy.client.generated.api.partners_api", "PartnersApi"),
    "PeopleApi": ("immichpy.client.generated.api.people_api", "PeopleApi"),
    "PluginsApi": ("immichpy.client.generated.api.plugins_api", "PluginsApi"),
    "QueuesApi": ("immichpy.client.generated.api.queues_api", "QueuesApi"),
    "SearchApi": ("immichpy.client.generated.api.search_api", "SearchApi"),
    "ServerApi": ("immichpy.client.generated.api.server_api", "ServerApi"),
    "SessionsApi": ("immichpy.client.generated.api.sessions_api", "SessionsApi"),
    "SharedLinksApi": (
        "immichpy.client.generated.api.shared_links_api",
        "SharedLinksApi",
    ),
    "StacksApi": ("immichpy.client.generated.api.stacks_api", "StacksApi"),
    "SyncApi": ("immichpy.client.generated.api.sync_api", "SyncApi"),
    "SystemConfigApi": (
        "immichpy.client.generated.api.system_config_api",
        "SystemConfigApi",
    ),
    "SystemMetadataApi": (
        "immichpy.client.generated.api.system_metadata_api",
        "SystemMetadataApi",
    ),
    "TagsApi": ("immichpy.client.generated.api.tags_api", "TagsApi"),
    "TimelineApi": ("immichpy.client.generated.api.timeline_api", "TimelineApi"),
    "TrashApi": ("immichpy.client.generated.api.trash_api", "TrashApi"),
    "UsersAdminApi": ("immichpy.client.generated.api.users_admin_api", "UsersAdminApi"),
    "UsersApi": ("immichpy.client.generated.api.users_api", "UsersApi"),
    "ViewsApi": ("immichpy.client.generated.api.views_api", "ViewsApi"),
    "WorkflowsApi": ("immichpy.client.generated.api.workflows_api", "WorkflowsApi"),
}


def __getattr__(name: str) -> object:
    try:
        module, attr = _LAZY_IMPORTS[name]
    except KeyError:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}") from None
    from importlib import import_module

    value = getattr(import_module(module), attr)
    globals()[name] = value
    return value
