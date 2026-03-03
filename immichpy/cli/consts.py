from pathlib import Path

DEVICE_ID = "immichpy"
"""The device ID for the CLI used for uploading assets."""
DEMO_API_URL = "https://demo.immich.app/api"
"""The Immich demo API URL."""
API_KEY_URL = "https://my.immich.app/user-settings?isOpen=api-keys"
"""The API key URL used for getting API keys."""
CONFIG_DIR = Path.home() / ".immichpy"
"""The config directory for the CLI."""
CONFIG_FILE = CONFIG_DIR / "config.toml"
"""The config file used for storing the CLI configuration."""
DEFAULT_PROFILE = "default"
"""The default profile for the CLI."""
DEFAULT_FORMAT = "pretty"
"""The default format for the CLI."""

# Environment variables
IMMICH_FORMAT = "IMMICH_FORMAT"
"""The environment variable for the format."""
IMMICH_API_URL = "IMMICH_API_URL"
"""The environment variable for the API URL."""
IMMICH_API_KEY = "IMMICH_API_KEY"  # nosec: B105
"""The environment variable for the API key."""
IMMICH_ACCESS_TOKEN = "IMMICH_ACCESS_TOKEN"  # nosec: B105
"""The environment variable for the access token."""
IMMICH_PROFILE = "IMMICH_PROFILE"
"""The environment variable for the profile."""

# Strings that indicate secret values
SECRET_KEYS = ["api_key", "access_token"]
"""The strings that indicate secret values."""
