#!/usr/bin/env python

import sys; sys.dont_write_bytecode = True
import platform
from bootstrap_helper import *
from user_editable import *

import subprocess

def printColors(): # Tentative
    printHeader("Header?")
    printBlue("Blue?")
    printGreen("Green?")
    printWarning("Warning?")
    printFail("Fail?")

class DotPlatform():
    def __init__(self, OS):
        self.OS = OS
    def getPackageList(self):
        if self.OS == "Linux":
            return UBUNTU_PACKAGE_LIST
        elif self.OS == "FreeBSD":
            return FREEBSD_PACAKAGE_LIST
    def getCommonConfigDir(self):
        return "./common_configs"
    def getPlatformConfigDir(self):
        if self.OS == "Linux":
            return "./linux_configs"
        elif self.OS == "FreeBSD":
            return "./bsd_configs"

if __name__ == "__main__":
#    printColors()
    dot_platform = DotPlatform(platform.system())
    manager = DotProcesser(platform.system(), IS_DISABLE_WARNING)
    manager.installPackages(dot_platform.getPackageList())
    manager.makeSymlinks(dot_platform.getCommonConfigDir())
#    manager.makeSymlinks(dot_platform.getPlatformConfigDir()) # No platform config yet
    manager.installCustoms() # Vundle, Prezto
