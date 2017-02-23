

import traceback

from subprocess import call, Popen, check_output

from build_configs import BUILD_COMMANDS

print BUILD_COMMANDS

for construct in BUILD_COMMANDS:

    for pre_set in construct.setup:
        print "$ ", ' '.join(pre_set)
        check_output(pre_set)

    print construct.desc
    try:
        out = check_output(construct.cmd)

        if construct.on_shell and out:
            print out

    except Exception as error:

        _err_tpl = construct.on_error % construct._asdict()

        print _err_tpl.format(str(error))
        print traceback.format_exc()

        # Break me building
        break

    else:
        print construct.on_success % construct._asdict()

    for reset in construct.teardown:
        print "$ ", ' '.join(reset)
        check_output(reset)
