from unittest.mock import patch

import pytest
import typer

from immich._internal.cli.utils import (
    _ensure_config,
    check_config,
    resolve_client_config,
    get_path,
    load_config,
    _is_secret_key,
    mask,
    _redact_secret,
    set_path,
    write_config,
)
from immich._internal.types import ClientConfig


class TestSetPath:
    def test_set_path_single_level(self):
        """Test setting a single-level path."""
        data = {}
        set_path(data, "name", "John")
        assert data == {"name": "John"}

    def test_set_path_nested(self):
        """Test setting a nested path."""
        data = {}
        set_path(data, "user.name", "John")
        assert data == {"user": {"name": "John"}}

    def test_set_path_overwrite_existing(self):
        """Test overwriting an existing value."""
        data = {"user": {"name": "John"}}
        set_path(data, "user.name", "Jane")
        assert data == {"user": {"name": "Jane"}}


class TestGetPath:
    def test_get_path_nested(self):
        """Test getting a nested path."""
        data = {"user": {"name": "John"}}
        assert get_path(data, "user.name") == "John"

    def test_get_path_key_error(self):
        """Test that KeyError is raised for missing keys."""
        data = {"user": {"name": "John"}}
        with pytest.raises(KeyError):
            get_path(data, "user.age")


class TestEnsureConfig:
    def test_ensure_config_creates_file(self, tmp_path):
        """Test that _ensure_config creates the config file and sets permissions."""
        config_dir = tmp_path / ".immich-py"
        config_file = config_dir / "config.toml"
        with patch("immich._internal.cli.utils.CONFIG_DIR", config_dir):
            with patch("immich._internal.cli.utils.CONFIG_FILE", config_file):
                _ensure_config()
                assert config_file.exists()
                assert oct(config_file.stat().st_mode)[-3:] == "600"

    def test_ensure_config_existing_file(self, tmp_path):
        """Test that _ensure_config handles existing file."""
        config_dir = tmp_path / ".immich-py"
        config_file = config_dir / "config.toml"
        config_dir.mkdir()
        config_file.write_text("existing content")
        with patch("immich._internal.cli.utils.CONFIG_DIR", config_dir):
            with patch("immich._internal.cli.utils.CONFIG_FILE", config_file):
                _ensure_config()
                assert config_file.read_text() == "existing content"


class TestLoadConfig:
    def test_load_config_with_ensure_exists(self, tmp_path):
        """Test load_config with ensure_exists=True creates file."""
        config_dir = tmp_path / ".immich-py"
        config_file = config_dir / "config.toml"
        with patch("immich._internal.cli.utils.CONFIG_DIR", config_dir):
            with patch("immich._internal.cli.utils.CONFIG_FILE", config_file):
                result = load_config(ensure_exists=True)
                assert config_file.exists()
                assert result == {}

    def test_load_config_without_ensure_exists(self, tmp_path):
        """Test load_config without ensure_exists on existing file."""
        config_dir = tmp_path / ".immich-py"
        config_file = config_dir / "config.toml"
        config_dir.mkdir()
        config_file.write_text('key = "value"')
        with patch("immich._internal.cli.utils.CONFIG_DIR", config_dir):
            with patch("immich._internal.cli.utils.CONFIG_FILE", config_file):
                result = load_config(ensure_exists=False)
                assert result == {"key": "value"}

    def test_load_config_file_not_exists_without_ensure(self, tmp_path):
        """Test load_config when file doesn't exist and ensure_exists=False."""
        config_dir = tmp_path / ".immich-py"
        config_file = config_dir / "config.toml"
        with patch("immich._internal.cli.utils.CONFIG_DIR", config_dir):
            with patch("immich._internal.cli.utils.CONFIG_FILE", config_file):
                with pytest.raises(FileNotFoundError):
                    load_config(ensure_exists=False)


class TestWriteConfig:
    def test_write_config_creates_file_and_sets_permissions(self, tmp_path):
        """Test that write_config creates the file and sets permissions."""
        config_dir = tmp_path / ".immich-py"
        config_file = config_dir / "config.toml"
        config_dir.mkdir()
        with patch("immich._internal.cli.utils.CONFIG_DIR", config_dir):
            with patch("immich._internal.cli.utils.CONFIG_FILE", config_file):
                write_config({"key": "value"})
                assert config_file.exists()
                assert config_file.read_text() == 'key = "value"\n'
                assert oct(config_file.stat().st_mode)[-3:] == "600"


class TestCheckConfig:
    def test_check_config_file_exists(self, tmp_path):
        """Test check_config when file exists."""
        config_dir = tmp_path / ".immich-py"
        config_file = config_dir / "config.toml"
        config_dir.mkdir()
        config_file.touch()
        with patch("immich._internal.cli.utils.CONFIG_FILE", config_file):
            result = check_config()
            assert result is True

    def test_check_config_file_not_exists(self, tmp_path):
        """Test check_config when file doesn't exist."""
        config_file = tmp_path / "config.toml"
        with patch("immich._internal.cli.utils.CONFIG_FILE", config_file):
            with patch("typer.echo") as mock_echo:
                with pytest.raises(typer.Exit) as exc_info:
                    check_config()
                assert exc_info.value.exit_code == 1
                mock_echo.assert_called_once()
                assert "Config file does not exist" in str(mock_echo.call_args[0][0])


class TestGetClientConfig:
    def test_get_client_config_from_file(self, tmp_path):
        """Test get_client_config loads from config file."""
        config_dir = tmp_path / ".immich-py"
        config_file = config_dir / "config.toml"
        config_dir.mkdir()
        config_file.write_text(
            '[profiles.default]\napi_key = "file-key"\nbase_url = "http://file.url"'
        )
        with patch("immich._internal.cli.utils.CONFIG_FILE", config_file):
            config = ClientConfig(api_key=None, base_url=None, access_token=None)
            result = resolve_client_config(config, profile="default")
            assert result.api_key == "file-key"
            assert result.base_url == "http://file.url"

    def test_get_client_config_prefers_provided_values(self, tmp_path):
        """Test that provided config values override file values."""
        config_dir = tmp_path / ".immich-py"
        config_file = config_dir / "config.toml"
        config_dir.mkdir()
        config_file.write_text(
            '[profiles.default]\napi_key = "file-key"\nbase_url = "http://file.url"'
        )
        with patch("immich._internal.cli.utils.CONFIG_FILE", config_file):
            config = ClientConfig(
                api_key="provided-key",
                base_url="http://provided.url",
                access_token=None,
            )
            result = resolve_client_config(config, profile="default")
            assert result.api_key == "provided-key"
            assert result.base_url == "http://provided.url"

    def test_get_client_config_partial_override(self, tmp_path):
        """Test that only provided values override file values."""
        config_dir = tmp_path / ".immich-py"
        config_file = config_dir / "config.toml"
        config_dir.mkdir()
        config_file.write_text(
            '[profiles.default]\napi_key = "file-key"\nbase_url = "http://file.url"\naccess_token = "file-token"'
        )
        with patch("immich._internal.cli.utils.CONFIG_FILE", config_file):
            config = ClientConfig(
                api_key="provided-key",
                base_url=None,
                access_token=None,
            )
            result = resolve_client_config(config, profile="default")
            assert result.api_key == "provided-key"
            assert result.base_url == "http://file.url"
            assert result.access_token == "file-token"

    def test_get_client_config_empty_file(self, tmp_path):
        """Test get_client_config with empty config file."""
        config_dir = tmp_path / ".immich-py"
        config_file = config_dir / "config.toml"
        config_dir.mkdir()
        config_file.touch()
        with patch("immich._internal.cli.utils.CONFIG_FILE", config_file):
            config = ClientConfig(api_key=None, base_url=None, access_token=None)
            with pytest.raises(typer.Exit):
                resolve_client_config(config, profile="default")

    def test_get_client_config_profile_not_in_file(self, tmp_path):
        """Test get_client_config when profile doesn't exist in file."""
        config_dir = tmp_path / ".immich-py"
        config_file = config_dir / "config.toml"
        config_dir.mkdir()
        config_file.write_text('[profiles.default]\napi_key = "default-key"')
        with patch("immich._internal.cli.utils.CONFIG_FILE", config_file):
            config = ClientConfig(api_key=None, base_url=None, access_token=None)
            with pytest.raises(typer.Exit):
                resolve_client_config(config, profile="nonexistent")


class TestRedactSecret:
    def test_redact_secret_empty_string(self):
        """Test redact_secret with empty string."""
        assert _redact_secret("") == ""

    def test_redact_secret_short_string(self):
        """Test redact_secret with string shorter than start + end."""
        assert _redact_secret("ab") == "**"
        assert _redact_secret("abc") == "***"


class TestIsSecretKey:
    def test_is_secret_key_api_key(self):
        """Test _is_secret_key with api_key."""
        assert _is_secret_key("api_key") is True
        assert _is_secret_key("my_api_key") is True
        assert _is_secret_key("api_key_value") is True

    def test_is_secret_key_access_token(self):
        """Test _is_secret_key with access_token."""
        assert _is_secret_key("access_token") is True
        assert _is_secret_key("my_access_token") is True
        assert _is_secret_key("access_token_value") is True

    def test_is_secret_key_not_secret(self):
        """Test _is_secret_key with non-secret keys."""
        assert _is_secret_key("base_url") is False
        assert _is_secret_key("profile") is False
        assert _is_secret_key("name") is False


class TestMask:
    def test_mask_dict_with_secret_string(self):
        """Test mask with dictionary containing secret string value."""
        obj = {"api_key": "mysecretkey123", "base_url": "http://example.com"}
        result = mask(obj)
        assert result == {"api_key": "mys********123", "base_url": "http://example.com"}

    def test_mask_dict_with_secret_non_string(self):
        """Test mask with dictionary containing secret key but non-string value."""
        obj = {"api_key": {"nested": "value"}, "base_url": "http://example.com"}
        result = mask(obj)
        assert result == {
            "api_key": {"nested": "value"},
            "base_url": "http://example.com",
        }

    def test_mask_dict_nested(self):
        """Test mask with nested dictionary."""
        obj = {"user": {"api_key": "secret123", "name": "John"}}
        result = mask(obj)
        assert result == {"user": {"api_key": "sec***123", "name": "John"}}

    def test_mask_list(self):
        """Test mask with list."""
        obj = [{"api_key": "secret123"}, {"name": "John"}]
        result = mask(obj)
        assert result == [{"api_key": "sec***123"}, {"name": "John"}]

    def test_mask_list_nested(self):
        """Test mask with nested list."""
        obj = {"items": [{"api_key": "secret123"}]}
        result = mask(obj)
        assert result == {"items": [{"api_key": "sec***123"}]}

    def test_mask_string_with_secret_key(self):
        """Test mask with top-level string and secret key."""
        result = mask("mysecretkey123", key="api_key")
        assert result == "mys********123"

    def test_mask_string_without_secret_key(self):
        """Test mask with top-level string and non-secret key."""
        result = mask("mysecretkey123", key="base_url")
        assert result == "mysecretkey123"

    def test_mask_string_without_key(self):
        """Test mask with top-level string without key."""
        result = mask("mysecretkey123")
        assert result == "mys********123"

    def test_mask_custom_start_end(self):
        """Test mask with custom start and end values."""
        obj = {"api_key": "mysecretkey123"}
        result = mask(obj, start=2, end=2)
        assert result == {"api_key": "my**********23"}

    def test_mask_multiple_secrets(self):
        """Test mask with multiple secret keys."""
        obj = {"api_key": "key123", "access_token": "token456"}
        result = mask(obj)
        assert result == {"api_key": "******", "access_token": "tok**456"}

    def test_mask_empty_dict(self):
        """Test mask with empty dictionary."""
        assert mask({}) == {}

    def test_mask_empty_list(self):
        """Test mask with empty list."""
        assert mask([]) == []

    def test_mask_other_types(self):
        """Test mask with other types (int, bool, None)."""
        assert mask(123) == 123
        assert mask(True) is True
        assert mask(None) is None
