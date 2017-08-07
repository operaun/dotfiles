# scripts/platform_helper.py

import os;
import sys; sys.dont_write_bytecode = True
from abc import ABCMeta, abstractmethod

# comment(jongmin): if multi level subdirectory is required, consider below sys.path.insert
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'other_dir'))
import user_editable

class PlatformHelperFactory(object):
    def factory(OS):
        if OS == "Linux": return LinuxPlatformHelper()
        elif OS == "FreeBSD": return FreeBSDPlatformHelper()
        assert 0, "Not supported OS classifiction: " + OS
    factory = staticmethod(factory)


class PlatformHelper(object):
    __metaclass__ = ABCMeta

    @classmethod
    def getCommonConfigDir(self):
        return os.path.join(os.path.dirname(__file__), '../common_configs')

    @classmethod
    def getWarningState(self): return user_editable.IS_DISABLE_WARNING

    @abstractmethod
    def getPlatformName(self): raise NotImplementedError

    @abstractmethod
    def getPackageList(self): raise NotImplementedError

    @abstractmethod
    def getPlatformConfigDir(self): raise NotImplementedError

    @abstractmethod
    def getInstallCommand(self): raise NotImplementedError


class LinuxPlatformHelper(PlatformHelper):
    def getPlatformName(self):
        return "Linux"
    def getPackageList(self):
        return user_editable.UBUNTU_PACKAGE_LIST
    def getPlatformConfigDir(self):
        return os.path.abspath("../linux_configs")
    def getInstallCommand(self):
        return "sudo apt-get install -y"


class FreeBSDPlatformHelper(PlatformHelper):
    def getPlatformName(self):
        return "FreeBSd"
    def getPackageList(self):
        return user_editable.FREEBSD_PACAKAGE_LIST
    def getPlatformConfigDir(self):
        return os.path.abspath("../bsd_configs")
    def getInstallCommand(self):
        return "sudo pkg install -y"
