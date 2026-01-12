"""Image and video generators for E2E tests."""

from __future__ import annotations

import io
from typing import Iterator

from PIL import Image


def _create_jpeg(r: int, g: int, b: int) -> bytes:
    """Create a minimal 1x1 JPEG with the specified RGB color."""
    img = Image.new("RGB", (1, 1), (r, g, b))
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG", quality=95)
    return buffer.getvalue()


def _new_jpeg_factory() -> Iterator[bytes]:
    """Generator that yields unique JPEG images by cycling through RGB values."""
    for r in range(0, 256, 16):  # Step by 16 to avoid too many combinations
        for g in range(0, 256, 16):
            for b in range(0, 256, 16):
                yield _create_jpeg(r, g, b)


_jpeg_factory = _new_jpeg_factory()


def make_random_image() -> bytes:
    """Generate a random unique JPEG image for testing."""
    global _jpeg_factory
    try:
        return next(_jpeg_factory)
    except StopIteration:
        # Reset factory if we run out
        _jpeg_factory = _new_jpeg_factory()
        return next(_jpeg_factory)


def _create_minimal_mp4(seed: int) -> bytes:
    """Create a minimal valid MP4 with variable seed data."""
    import base64

    # Use the original minimal MP4 template (valid MP4 header)
    # This is a minimal valid MP4 file that Immich can process
    mp4_base64 = "AAAAIGZ0eXBtcDQyAAAAAG1wNDJtcDQxaXNvbWF2YzEAAAGhtZGF0AAACrgYF//+q3EXpvebZSLeWLNgg2SPu73gyNjQgLSBjb3JlIDE0OCByMjA1OCBlYjc2Y2U1IC0gSC4yNjQvTVBFRy00IEFWQyBjb2RlYyAtIENvcHlsZWZ0IDIwMDMtMjAxNyAtIGh0dHA6Ly93d3cudmlkZW9sYW4ub3JnL3gyNjQuaHRtbCAtIG9wdGlvbnM6IGNhYmFjPTEgcmVmPTMgZGVibG9jaz0xOjA6MCBhbmFseXNlPTB4MzoweDExMyBtZT1oZXggc3VibWU9NyBwc3k9MSBwc3lfcmQ9MS4wMDowLjAwIG1peGVkX3JlZj0xIG1lX3JhbmdlPTE2IGNocm9tYV9tZT0xIHRyZWxsaXM9MSA4eDhkY3Q9MSBjcW09MCBkZWFkem9uZT0yMSwxMSBmYXN0X3Bza2lwPTEgY2hyb21hX3FwX29mZnNldD0tMiB0aHJlYWRzPTEgbG9va2FoZWFkX3RocmVhZHM9MSBzbGljZWRfdGhyZWFkcz0wIG5yPTAgZGVjaW1hdGU9MSBpbnRlcmxhY2VkPTAgYmx1cmF5X2NvbXBhdD0wIGNvbnN0cmFpbmVkX2ludHJhPTAgYmZyYW1lcz0zIGJfcHlyYW1pZD0yIGJfYWRhcHQ9MSBiX2JpYXM9MCBkaXJlY3Q9MSB3ZWlnaHRiPTEgb3Blbl9nb3A9MCB3ZWlnaHRwPTIga2V5aW50PTI1MCBrZXlpbnRfbWluPTI1IHNjZW5lY3V0PTQwIGludHJhX3JlZnJlc2g9MCByY19sb29rYWhlYWQ9NDAgcmM9Y3JmIG1idHJlZT0xIGNyZj0yMy4wIHFjb21wPTAuNjAgcXBtaW49MCBxcG1heD02OSBxcHN0ZXA9NCBpcF9yYXRpbz0xLjQwIGFxPTE6MS4wMAA="
    mp4_bytes = bytearray(base64.b64decode(mp4_base64))

    # Make each MP4 unique by replacing a section with seed-based data
    # Replace bytes in multiple locations to ensure significant content difference
    seed_bytes = seed.to_bytes(8, byteorder="big")
    # Modify multiple sections to ensure uniqueness
    offsets = [100, 200, 300, 400]
    for offset in offsets:
        if offset < len(mp4_bytes) - len(seed_bytes):
            for i, byte_val in enumerate(seed_bytes):
                if offset + i < len(mp4_bytes):
                    # Replace with seed data to ensure uniqueness
                    mp4_bytes[offset + i] = (
                        mp4_bytes[offset + i] + byte_val + seed
                    ) % 256

    return bytes(mp4_bytes)


def _new_mp4_factory() -> Iterator[bytes]:
    """Generator that yields unique MP4 videos by incrementing seed."""
    seed = 0
    while True:
        yield _create_minimal_mp4(seed)
        seed = (seed + 1) % (2**32)


_mp4_factory = _new_mp4_factory()


def make_random_video() -> bytes:
    """Generate a random unique MP4 video for testing."""
    return next(_mp4_factory)
