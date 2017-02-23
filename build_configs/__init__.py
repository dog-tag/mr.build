
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


BUILD_COMMANDS = [

    build_command(
        cmd=('ls', '-la', ),
        desc='Listing all the files and folders...',
        on_success='Command %(cmd)s ran successfully !',
        on_error='Command %(cmd)s failed !. ERROR: {}',
    ),

    build_command(
        cmd=('wget', 'www.google.com', ),
        setup=[
            ('cd', 'downloads/', )
        ],
        teardown=[
            ('cd', '../', )
        ],
        desc='Fetching Python',
        on_success='Command %(cmd)s ran successfully !',
        on_error='Command %(cmd)s failed !. ERROR: {}',
    ),

]
