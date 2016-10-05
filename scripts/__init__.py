#!/usr/bin/env python

import os;
import sys; sys.dont_write_bytecode = True
import platform

# comment(jongmin): if multi level subdirectory is required, consider below sys.path.insert
#sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), 'scripts'))
import platform_helper
import dot_helper

def printColors(): # Tentative
    printHeader("Header?")
    printBlue("Blue?")
    printGreen("Green?")
    printWarning("Warning?")
    printFail("Fail?")

def dot_main(args):
#    printColors()
    helper = platform_helper.PlatformHelperFactory.factory(platform.system())
    processor = dot_helper.DotProcesser(platform.system(), helper.getWarningState())
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
