#!/usr/bin/env python

import os
import subprocess

class CustomPackageManager:
    def installDefaultZsh(self):
        zsh_file_path = readStringFromCmd("which zsh")
        if (zsh_file_path == False):
            printHeader("Can not find zsh installation")
        printHeader("Your new default shell path($SHELL): %s" % zsh_file_path)
        os.system("chsh -s %s" % zsh_file_path)

    def installVimColor(self):
        os.system("mkdir -p ~/.vim/colors")
        os.system("cp ./custom_files/jellybeans.vim ~/.vim/colors/")

    def installVundle(self):
        os.system("mkdir -p ~/.vim/bundle")
        os.system("git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim")
        os.system("vim +PluginInstall +qall")


class DotProcesser:
    # Several functionalities are not arranged yet
    # installPackages
    # installCustoms
    # makeSymlinks

    def __init__(self, OS, disable_warning):
        self.OS = OS
        self.disable_warning = disable_warning
        self.home_dir = os.path.expanduser('~')

        printHeader("Your OS: %s" % self.OS)
        printHeader("Your home directory: %s" % self.home_dir)
        printHeader("Disable warning: %s" % disable_warning)
        printDefault("")

    def confirmContinue(self):
        if (self.disable_warning is True):
            return True 
        if ("y" == raw_input(bcolors.WARNING + "y/n?: " + bcolors.ENDC)):
            return True
        return False

    def installPackage(self, package):
        if self.OS == "Linux": # Ubuntu
            subprocess.call(["sudo", "apt-get", "install", "-y", package])
        elif self.OS == "FreeBSD":
            subprocess.call(["pkg", "install", "-y", package])

    def installPackages(self, packages):
        printGreen("--| Try to install/update following packages")
        package_list = packages.splitlines()
        for package in package_list:
            printBlue("\t " + package)

        if (self.confirmContinue() is False):
            printWarning("Do not do it")
            return

        for package in package_list:
            self.installPackage(package)
        printDefault("")

    def installCustoms(self):
        printGreen("\n--| Install custom programs from -- ")
        printBlue("\t Jellybeans color: color for VIM")
        printBlue("\t Vundle: plugin framework for VIM")
        printBlue("\t Default Zsh: change $SHELL config")
        if (self.confirmContinue() is False):
            printWarning("Do not do it")
            return
        custom_package_manager = CustomPackageManager()
        custom_package_manager.installVimColor()
        custom_package_manager.installVundle()
        custom_package_manager.installDefaultZsh()

    def makeSymlinkWith(self, config_file, config_dir):
        source_path = "%s/%s" % (config_dir, config_file)
        target_path = self.home_dir + "/.%s" % config_file
#        if (config_file.hasCustomPath() == true):
#            target_path = config_file.CustomPath()
        os.system( "ln -sfnv %s %s" % (source_path, target_path) )

    def makeSymlinksFromDir(self, config_dir):
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

    def makeSymlinks(self, config_dir):
#        self.makeSymlinksFromDir(os.path.abspath("./common_configs"))
        self.makeSymlinksFromDir(os.path.abspath(config_dir))
#        if self.OS == "Linux": # Ubuntu
#            self.makeSymlinksFromDir(os.path.abspath("./linux_configs"))
#        elif self.OS == "FreeBSD":
#            self.makeSymlinksFromDir(os.path.abspath("./bsd_configs"))


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def printHeader(string):
    print(bcolors.HEADER + string + bcolors.ENDC)

def printBlue(string):
    print(bcolors.OKBLUE + string + bcolors.ENDC)

def printGreen(string):
    print(bcolors.OKGREEN + string + bcolors.ENDC)

def printWarning(string):
    print(bcolors.WARNING + string + bcolors.ENDC)

def printFail(string):
    print(bcolors.FAIL + string + bcolors.ENDC)

def printDefault(string):
    print(string)


def readStringFromCmd(cmd):
    ret_string = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).stdout.readline()
    if len(ret_string) == 0:
        return False
    return ret_string
