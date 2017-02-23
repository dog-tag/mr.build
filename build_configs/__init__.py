
import os

PY_VERSION = '2.7.13'

from collections import namedtuple

def build_command(cmd,
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

    Runnable = namedtuple(
        'Runnable',
        'cmd, setup, teardown, mode, log, desc, on_shell, on_success, on_error'
    )

    return Runnable(
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


class ChangeDir(object):
    def __init__(self, target):
        self.target = target


BUILD_COMMANDS = [

    build_command(
        cmd=('ls', '-la', ),
        desc='Listing all the files and folders...',
        on_success='Command %(cmd)s ran successfully !',
        on_error='Command %(cmd)s failed !. ERROR: {}',
    ),

    #
    # Install Python as Virtual Environment.
    build_command(
        cmd=('ls'),  #'wget', '-P', 'downloads/', 'https://www.python.org/ftp/python/{0}/Python-{0}.tar.xz'.format(PY_VERSION), ),
        setup=[
            ('cd', 'downloads/', )
        ],
        teardown=[
            ChangeDir('downloads/'),
            ('tar', '-xvJf', 'Python-{0}.tar.xz'.format(PY_VERSION)),
            ChangeDir('downloads/Python-{0}/'.format(PY_VERSION)),
            ('./configure', '--prefix={0}/usr/'.format(os.getcwd()), '--enable-unicode=ucs4'),
            ChangeDir('downloads/Python-{0}/'.format(PY_VERSION)),
            ('make'),
            ChangeDir('downloads/Python-{0}/'.format(PY_VERSION)),
            ('make', 'install'),
            ChangeDir('../'),
            ('rm', '-rvf', 'downloads/Python-{0}/'.format(PY_VERSION), ),
            ChangeDir('../'),
        ],
        desc='Fetching Python',
        on_success='Command %(cmd)s ran successfully !',
        on_error='Command %(cmd)s failed !. ERROR: {}',
    ),

]
