# -*- coding: utf-8 -*-

"""Linux script.

This module holds the commands to install necessary packages
on windows platform.

Example:
    * To be completed... 

Todo:
    * To be completed...

"""
# --------------- START: Native Imports -------------- #
import os
# --------------- END: Native Imports -------------- #

# --------------- START: In-House Imports -------------- #
from utils.commons import (
    ChangeDir, AbortBuild, TextMessage, build_expr, simple_command, complex_command
)
# --------------- END: In-House Imports -------------- #


__all__ = [
    # Public Symbols.
]


PY_VERSION = '2.7.13'
"""``str``: Module level variable.  Version number for the python.
"""


BUILD_COMMANDS = list()
