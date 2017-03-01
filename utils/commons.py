# -*- coding: utf-8 -*-

"""Commons script.

It's a collection of utility methods and classes 
for the project.

Todo:
    * To be completed...

"""

# --------------- START: Native Imports -------------- #
from collections import namedtuple
# --------------- END: Native Imports -------------- #

def build_expr(cmd,
                  setup=None,
                  teardown=None,
                  mode='fg',
                  log=True,
                  desc=None,
                  on_shell=True,
                  on_success=None,
                  on_error=None):

    """."""

    if not isinstance(cmd, (str, list, tuple)):
        raise Exception()

    if mode not in ('fg', 'bg', ):
        raise Exception()

    if not isinstance(log, bool):
        raise Exception()

    setup = setup or list()
    teardown = teardown or list()

    BuildExpr = namedtuple(
        'BuildExpr',
        'cmd, setup, teardown, mode, log, desc, on_shell, on_success, on_error'
    )

    return BuildExpr(
        cmd=cmd,
        setup=setup,
        teardown=teardown,
        mode=mode,
        log=log,
        desc=desc,
        on_shell=on_shell,
        on_success=on_success,
        on_error=on_error
    )


SimpleCommand = namedtuple('SimpleCommand', 'cmd')
ComplexCommand = namedtuple('ComplexCommand', 'if_, if_axn, else_axn')

def simple_command(cmd):
    """."""
    return SimpleCommand(cmd=cmd.split())

def complex_command(if_=None, if_axn=None, else_axn=None):
    """."""
    if_ = if_ and if_.split()
    if_axn = if_axn.split() if isinstance(if_axn, str) else if_axn
    else_axn = else_axn.split() if isinstance(else_axn, str) else else_axn

    return ComplexCommand(if_=if_, if_axn=if_axn, else_axn=else_axn)


class ChangeDir(object):
    """."""
    def __init__(self, target=None):
        self.target = target


class TextMessage(object):
    """."""
    def __init__(self, msg):
        self.message = msg


class AbortBuild(object):
    """."""
    def __init__(self, message):
        self.message = message


