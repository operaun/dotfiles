# scripts/dot_helper.py

import os
import subprocess
import custom_task_manager
from pretty_printer import *

class DotProcesser(object):
    # Several functionalities are not arranged yet
    # installPackages
    # installCustoms
    # makeSymlinks

    def __init__(self, OS, disable_warning):
        self.disable_warning = disable_warning
        self.home_dir = os.path.expanduser('~')

        printHeader("Your OS: %s" % OS)
        printHeader("Your home directory: %s" % self.home_dir)
        printHeader("Disable warning: %s" % disable_warning)
        printDefault("")

    def confirmContinue(self):
        if (self.disable_warning is True):
            return True 
        if ("y" == raw_input(bcolors.WARNING + "y/n?: " + bcolors.ENDC)):
            return True
        return False

    def installPackage(self, package, cmd):
        PrintDefault(cmd + " %s" % package)
        subprocess.call(cmd + " %s" % package, shell=True)

    def installPackages(self, packages, cmd):
        printGreen("--| Try to install/update following packages")
        package_list = packages.splitlines()
        for package in package_list:
            printBlue("\t " + package)

        if (self.confirmContinue() is False):
            printWarning("Do not do it")
            return

        for package in package_list:
            self.installPackage(package, cmd)
        printDefault("")

    def installCustoms(self):
        task_manager = custom_task_manager.CustomTaskManager()
        # task_manager.addTask(custom_task_manager.VimUpdateTask()) # now only support ubuntu
        task_manager.addTask(custom_task_manager.VimColorTask())
        task_manager.addTask(custom_task_manager.VimVundleTask())
        task_manager.addTask(custom_task_manager.ZshTask())
        task_manager.addTask(custom_task_manager.GitConfigTask())

        printGreen("\n--| Install custom programs from -- ")
        task_manager.printMessages()
        if (self.confirmContinue() is False):
            printWarning("Do not do it")
            return
        task_manager.doWorks()

    def makeSymlinkWith(self, config_file, config_dir):
        source_path = "%s/%s" % (config_dir, config_file)
        target_path = self.home_dir + "/.%s" % config_file
#        if (config_file.hasCustomPath() == true):
#            target_path = config_file.CustomPath()
        os.system( "ln -sfnv %s %s" % (source_path, target_path) )

    def makeSymlinks(self, config_dir):
        config_dir = os.path.abspath(config_dir)
        config_files = os.listdir(config_dir)
        if (len(config_files) == 0): # if config_dir is empty, just return
            return

        printGreen("\n--| Try to make symbolic links from %s" % config_dir)
        for config_file in config_files:
            printBlue("\t " + config_file)

        if (self.confirmContinue() is False):
            printWarning("Do not do it")
            return

        for config_file in config_files:
            self.makeSymlinkWith(config_file, config_dir)
