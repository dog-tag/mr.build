# -*- coding: utf-8 -*-

"""Configs Package.
"""


# --------------- START: Native Imports -------------- #
import os

from ConfigParser import SafeConfigParser
# --------------- END: Native Imports -------------- #


# --------------- START: In-House Imports -------------- #
from utils.commons import (
    ChangeDir, AbortBuild, TextMessage, build_expr, simple_command, complex_command
)
# --------------- END: In-House Imports -------------- #


__all__ = [
    # Public Symbols.
]


class IniParser(object):

    def __init__(self, f_path):

        self.parser = SafeConfigParser()
        self.parser.read(os.path.join(os.getcwd(), f_path))

    def __call__(self, section, option):

        return self.parser.get(section, option)


versions_config = IniParser('configs/versions.ini')
