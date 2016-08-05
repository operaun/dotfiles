#!/usr/bin/env python

import sys; sys.dont_write_bytecode = True
import platform
from bootstrap_helper import *
from user_editable_list import *

import subprocess

def printColors():
    printHeader("Header?")
    printBlue("Blue?")
    printGreen("Green?")
    printWarning("Warning?")
    printFail("Fail?")

if __name__ == "__main__":
#    printColors()
    current_system = platform.system()
    manager = DotSystemManager(current_system, False)
    if current_system == "Linux": # Ubuntu
        manager.installPackages(UBUNTU_PACKAGE_LIST)
    elif current_system == "FreeBSD":
        manager.installPackages(FREEBSD_PACAKAGE_LIST)
    manager.installCustoms() # Vundle, Prezto
    manager.makeSymlinks()
