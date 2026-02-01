## Versioning Model

This package follows **[Semantic Versioning](https://semver.org)**.
The package version (`x.y.z`) represents the **client library**, not the Immich server. Version numbers communicate **client impact and server compatibility**, not just upstream change size.


## How Releases Are Versioned

Version bumps reflect changes to:

1. The **client’s public Python API**, and
2. The **minimum supported Immich server version**

| Bump | Meaning |
|------|---------|
| **Major** | Breaking change to the client API **or** the **minimum supported Immich server version increases** |
| **Minor** | Backward-compatible additions that still work with all previously supported server versions |
| **Patch** | Bug fixes or internal updates that do not change the client API or server compatibility |

!!! tip "A major version signals:"
    **“This client now requires a newer Immich server.”**


## Client–Server Compatibility

This client uses strict Pydantic models generated from a specific Immich server schema.

|  | Used with **older** server | Used with **newer** server |
|-------------------|------------------------|------------------------|
| **Older client**  | ✅ Works | ✅ Works (extra server fields are ignored) |
| **Newer client**  | ❌ May fail (server may not provide required fields) | ✅ Works |

!!! tip "Rule of thumb"
    Use a client version generated from the **same or an older Immich server version** than the one you are running.


## Minimum Supported Server Version

Every client release defines a **minimum supported Immich server version**.
If a release requires server behavior that older servers cannot provide, the minimum supported server version increases.

When this happens, the release is considered **breaking** and results in a **major** version bump.

**Example**

- Server **2.5.0** introduces a new required response field
- Client models now require this field
- Servers **2.4.x** cannot provide it

Result:

| Client Version | Minimum Supported Server |
|----------------|--------------------------|
| 1.6.x | 2.4.x |
| **2.0.0** | **2.5.0** |

Upgrading from `1.x` → `2.x` means you are choosing to require Immich server ≥ 2.5.0.


## Immich Server Compatibility Tracking

Server compatibility is tracked in [`COMPATIBILITY.csv`](https://github.com/timonrieger/immichpy/blob/main/COMPATIBILITY.csv).

| Column | Meaning |
|--------|---------|
| **Package version** | Version of this client library (`immichpy`) |
| **Generated from Immich server version** | Immich server version whose schema was used to generate the client |
| **Minimum supported Immich server version** | Oldest Immich server version guaranteed to work with this client |
| **Status** | Indicates if the version is current, superseded, or part of the legacy `immich` package |

The [`IMMICH-VERSION`](https://github.com/timonrieger/immichpy/blob/main/IMMICH-VERSION) file records the server version used for generation in the current source tree.
