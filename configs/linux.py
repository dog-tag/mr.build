
import os

PY_VERSION = '2.7.13'

from utils.commons import (
    ChangeDir, AbortBuild, TextMessage, build_expr, simple_command, complex_command
)

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
            simple_command('./configure --prefix={0}/usr/ --enable-unicode=ucs4'.format(os.getcwd())),
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
