#!/usr/bin/env python

import os;
import sys; sys.dont_write_bytecode = True
import platform
import argparse

# comment(jongmin): if multi level subdirectory is required, consider below sys.path.insert
#sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), 'scripts'))
import platform_helper
import dot_helper

def GetArgumentParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-y', '--yes', action="store_true",
            help='disabling warning as if you type yes for all given selection')
    return parser.parse_args()

def dot_main(args):
    parser = GetArgumentParser()
    helper = platform_helper.PlatformHelperFactory.factory(platform.system())

    disabling_warning = helper.getWarningState()
    if (parser.yes):
       disabling_warning = True

    processor = dot_helper.DotProcesser(helper.getPlatformName(), helper.getWarningState())
    processor.installPackages(helper.getPackageList(), helper.getInstallCommand())
    processor.makeSymlinks(helper.getCommonConfigDir())
#    processor.makeSymlinks(helper.getPlatformConfigDir()) # No platform config yet
    processor.installCustoms() # Vundle, Prezt

def main(args):
#    try:
    return dot_main(args)
#    except Exception, e:
#        sys.stderr.write("dot: %s\n" % e)
#        return 1

def script_main():
    return main(sys.argv[1:])

if __name__ == '__main__':
    sys.exit(script_main())
