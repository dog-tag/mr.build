# -*- coding: utf-8 -*-

"""Initial buildme script.

This module demonstrates that how to run this build, which sets up the basic
platform for the project.

Example:
        $ python buildme.py

Todo:
    * To be completed...

"""

# --------------- START: Native Imports -------------- #
import os
import traceback

from pprint import pprint as pp
from subprocess import call, Popen, check_output
# --------------- END: Native Imports -------------- #

# --------------- START: Third-Party Imports -------------- #
# --------------- END: Third-Party Imports -------------- #

# --------------- START: In-House Imports -------------- #
# TODO: patched for Windows
from configs.linux import BUILD_COMMANDS

from utils.commons import (
    ChangeDir, ComplexCommand, SimpleCommand, TextMessage, AbortBuild
)
# --------------- END: In-House Imports -------------- #


__all__ = [
    # Public Symbols.
]


BUILD_DIR = os.getcwd()
"""``str``: Module level variable.  Absolute path to the BUILD Directory.
"""


def execute(cmd):

    """."""

    if isinstance(cmd, AbortBuild):
        raise Exception(cmd.message)
    return check_output(cmd)


def test_execute(cmd):

    """."""

    return bool(check_output(cmd))


def evaluate(command_list):

    """."""

    for command in command_list:
        print ">>>", command
        if isinstance(command, ChangeDir):
            if command.target:
                change_to = os.path.join(BUILD_DIR, command.target)
            else:
                change_to = BUILD_DIR

            os.chdir(change_to)

        if isinstance(command, SimpleCommand):
            print execute(command.cmd)

        if isinstance(command, ComplexCommand):

            if command.if_ and test_execute(command.if_):
                if command.if_axn:
                    if isinstance(command.if_axn, TextMessage):
                        print command.if_axn.message
                    else:
                        print execute(command.if_axn)
            elif command.else_axn:
                if isinstance(command.else_axn, TextMessage):
                    print command.else_axn
                else:
                    print execute(command.else_axn)


for construct in BUILD_COMMANDS:

    if construct.setup:
        pass

    if construct.setup:
        evaluate(construct.setup)

    if construct.cmd:
        evaluate(construct.cmd)

    if construct.teardown:
        evaluate(construct.teardown)
