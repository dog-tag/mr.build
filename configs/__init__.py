
import os

PY_VERSION = '2.7.13'

from collections import namedtuple

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
    return SimpleCommand(cmd=cmd.split())

def complex_command(if_=None, if_axn=None, else_axn=None):

    if_ = if_ and if_.split()
    if_axn = if_axn.split() if isinstance(if_axn, str) else if_axn
    else_axn = else_axn.split() if isinstance(else_axn, str) else else_axn

    return ComplexCommand(if_=if_, if_axn=if_axn, else_axn=else_axn)


class ChangeDir(object):
    def __init__(self, target=None):
        self.target = target


class TextMessage(object):
    def __init__(self, msg):
        self.message = msg


class AbortBuild(object):
    def __init__(self, message):
        self.message = message


BUILD_COMMANDS = [

    #
    # Install Python as Virtual Environment.
    build_expr(

        desc='Downloading and installing Custom Python version'.format(PY_VERSION),

        cmd=[
            complex_command(
                if_='find usr/bin/ -name python',
                if_axn=AbortBuild('Python is already installed !, please remove the  existing one.'),
                else_axn=TextMessage('New Python will be installed !')
            ),
            complex_command(
                if_='find downloads/ -name Python-{0}.tar.xz'.format(PY_VERSION),
                if_axn=TextMessage('Download Exists -- Python-{0}.tar.xz'.format(PY_VERSION)),
                else_axn='wget -P downloads/ https://www.python.org/ftp/python/{0}/Python-{0}.tar.xz'.format(PY_VERSION)
            ),
            ChangeDir('downloads/'),
            simple_command('tar -xvJf Python-{0}.tar.xz'.format(PY_VERSION)),
            ChangeDir('downloads/Python-{0}/'.format(PY_VERSION)),
            simple_command('./configure --prefix={0}/usr/ --enable-unicode=ucs4 --enable-optimizations'.format(os.getcwd())),
            simple_command('make'),
            simple_command('make install'),
        ],

        teardown=[
            ChangeDir(),
            simple_command('rm -rvf downloads/Python-{0}/'.format(PY_VERSION)),
        ],

        on_success='Command %(cmd)s ran successfully !',
        on_error='Failed while running the command %(cmd)s. ERROR: {}',
    ),

]
