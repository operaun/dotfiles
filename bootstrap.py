#!/usr/bin/env python

import sys; sys.dont_write_bytecode = True
import platform
from bootstrap_helper import *
from user_editable_list import PACKAGE_LIST

def printColors():
    printHeader("Header?")
    printBlue("Blue?")
    printGreen("Green?")
    printWarning("Warning?")
    printFail("Fail?")

if __name__ == "__main__":
#    printColors()
    manager = DotSystemManager(platform.system(), True)
    manager.installPackages(PACKAGE_LIST)
    manager.installCustoms() # Vundle, Prezto
    manager.makeSymlinks()
