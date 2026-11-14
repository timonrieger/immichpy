"""File birth time on Linux via the statx(2) syscall, which `os.stat` does not expose."""

from __future__ import annotations

import ctypes
import os
import platform

# statx(2) syscall number per architecture, from the kernel syscall tables
_SYSCALL_NUMBERS: dict[str, int] = {
    "x86_64": 332,
    "aarch64": 291,
    "riscv64": 291,
    "i386": 383,
    "i686": 383,
    "armv7l": 397,
    "ppc64le": 383,
    "s390x": 379,
}
_AT_FDCWD = -100
_STATX_BTIME = 0x800


class _StatxTimestamp(ctypes.Structure):
    _fields_ = [
        ("tv_sec", ctypes.c_int64),
        ("tv_nsec", ctypes.c_uint32),
        ("_reserved", ctypes.c_int32),
    ]


class _Statx(ctypes.Structure):
    """`struct statx` from include/uapi/linux/stat.h (256 bytes)."""

    _fields_ = [
        ("stx_mask", ctypes.c_uint32),
        ("stx_blksize", ctypes.c_uint32),
        ("stx_attributes", ctypes.c_uint64),
        ("stx_nlink", ctypes.c_uint32),
        ("stx_uid", ctypes.c_uint32),
        ("stx_gid", ctypes.c_uint32),
        ("stx_mode", ctypes.c_uint16),
        ("_spare0", ctypes.c_uint16),
        ("stx_ino", ctypes.c_uint64),
        ("stx_size", ctypes.c_uint64),
        ("stx_blocks", ctypes.c_uint64),
        ("stx_attributes_mask", ctypes.c_uint64),
        ("stx_atime", _StatxTimestamp),
        ("stx_btime", _StatxTimestamp),
        ("stx_ctime", _StatxTimestamp),
        ("stx_mtime", _StatxTimestamp),
        ("_rest", ctypes.c_uint8 * 128),
    ]


def birthtime(path: str) -> float | None:
    """Return the birth time of a file in seconds since the epoch.

    :param path: The path to the file.

    :return: The birth time, or None if the platform or filesystem does not provide it.
    """
    # TODO: drop the ctypes call once Python 3.15 (which adds os.statx) is the minimum
    if hasattr(os, "statx"):
        try:
            return os.statx(path, os.STATX_BTIME).stx_btime
        except OSError:
            return None
    number = _SYSCALL_NUMBERS.get(platform.machine())
    if platform.system() != "Linux" or number is None:
        return None
    buf = _Statx()
    result = ctypes.CDLL(None).syscall(
        ctypes.c_long(number),
        ctypes.c_int(_AT_FDCWD),
        ctypes.c_char_p(os.fsencode(path)),
        ctypes.c_int(0),
        ctypes.c_uint(_STATX_BTIME),
        ctypes.byref(buf),
    )
    if result != 0 or not buf.stx_mask & _STATX_BTIME:
        return None
    return buf.stx_btime.tv_sec + buf.stx_btime.tv_nsec / 1e9
