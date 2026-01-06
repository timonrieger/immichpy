from __future__ import annotations


import pytest

import immich.utils as utils


def test_filename_from_headers_prefers_content_disposition() -> None:
    headers = {"Content-Disposition": 'attachment; filename="hello.jpg"'}
    assert utils.filename_from_headers(headers, fallback_base="ignored") == "hello.jpg"


def test_filename_from_headers_uses_content_type_as_extension_safety_net_for_cd_name() -> (
    None
):
    headers = {
        "Content-Disposition": 'attachment; filename="hello"',
        "Content-Type": "image/jpeg",
    }
    assert utils.filename_from_headers(headers, fallback_base="ignored") == "hello.jpg"


def test_filename_from_headers_cd_without_extension_and_without_content_type_returns_bare_cd_name() -> (
    None
):
    headers = {"Content-Disposition": 'attachment; filename="hello"'}
    assert utils.filename_from_headers(headers, fallback_base="ignored") == "hello"


def test_filename_from_headers_falls_back_to_content_type() -> None:
    headers = {"Content-Type": "image/jpeg"}
    assert (
        utils.filename_from_headers(headers, fallback_base="orig-123") == "orig-123.jpg"
    )


def test_filename_from_headers_returns_none_when_content_type_is_unknown_and_no_cd_name() -> (
    None
):
    headers = {"Content-Type": "application/x-unknown"}
    assert utils.filename_from_headers(headers, fallback_base="orig-123") is None


def test_filename_from_headers_returns_none_when_no_cd_and_no_content_type() -> None:
    headers = {"X-Other": "1"}
    assert utils.filename_from_headers(headers, fallback_base="orig-123") is None


def test_filename_from_headers_none_headers() -> None:
    assert utils.filename_from_headers(None, fallback_base="orig-123") is None


@pytest.mark.parametrize(
    ("name", "default_ext", "headers", "expected"),
    [
        # user name wins; path + extension are stripped; extension comes from Content-Type
        ("dir/evil.png", None, {"Content-Type": "image/jpeg"}, "evil.jpg"),
        ("image.txt", None, {"Content-Type": "image/jpeg"}, "image.jpg"),
        # user name with no ext gets content-type ext (when default_ext is not forcing)
        ("photo", None, {"Content-Type": "image/jpeg"}, "photo.jpg"),
        # user name with no ext and no content-type => keep as-is
        ("photo", None, None, "photo"),
        # user name with ext and no content-type => strip ext
        ("photo.txt", None, None, "photo"),
        # forcing default_ext strips any ext
        ("foo.tar.gz", ".zip", None, "foo.tar.zip"),
        ("foo.tar.gz", ".zip", {"Content-Type": "image/jpeg"}, "foo.tar.zip"),
        # header-derived name is used when no user name
        (
            None,
            None,
            {"Content-Disposition": 'attachment; filename="abc.jpeg"'},
            "abc.jpeg",
        ),
        # forcing default_ext also applies to header-derived name
        (
            None,
            ".zip",
            {"Content-Disposition": 'attachment; filename="abc.jpeg"'},
            "abc.zip",
        ),
        # header-derived name without ext (and no Content-Type ext) yields base only
        (None, None, {"Content-Disposition": 'attachment; filename="abc"'}, "abc"),
        # default is used when neither user name nor header name is available
        (None, None, None, "orig-123"),
        (None, ".zip", None, "archive-x.zip"),
    ],
)
def test_resolve_output_filename(
    name: str | None,
    default_ext: str | None,
    headers: dict[str, str] | None,
    expected: str,
) -> None:
    default_base = "archive-x" if expected.startswith("archive-x") else "orig-123"
    assert (
        utils.resolve_output_filename(
            headers,
            name=name,
            default_base=default_base,
            default_ext=default_ext,
        )
        == expected
    )


def test_resolve_output_filename_rejects_default_ext_without_dot() -> None:
    with pytest.raises(ValueError, match="default_ext must start with"):
        utils.resolve_output_filename(
            None, name=None, default_base="x", default_ext="zip"
        )
