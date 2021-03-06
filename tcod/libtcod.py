"""This module handles loading of the libtcod cffi API.
"""
import sys
import os

import platform

from tcod import __path__

if sys.platform == "win32":
    # add Windows dll's to PATH
    _bits, _linkage = platform.architecture()
    os.environ["PATH"] = "%s;%s" % (
        os.path.join(__path__[0], "x86" if _bits == "32bit" else "x64"),
        os.environ["PATH"],
    )


class _Mock(object):
    """Mock object needed for ReadTheDocs."""

    CData = ()  # This gets passed to an isinstance call.

    @staticmethod
    def def_extern():
        """Pass def_extern call silently."""
        return lambda func: func

    def __getattr__(self, attr):
        """This object pretends to have everything."""
        return self

    def __call__(self, *args, **kargs):
        """Suppress any other calls"""
        return self

    def __str__(self):
        """Just have ? in case anything leaks as a parameter default."""
        return "?"


if os.environ.get("READTHEDOCS"):
    # Mock the lib and ffi objects needed to compile docs for readthedocs.io
    # Allows an import without building the cffi module first.
    lib = ffi = _Mock()
else:
    from tcod._libtcod import lib, ffi  # noqa: F401

__all__ = ["ffi", "lib"]
