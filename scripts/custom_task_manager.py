#!/usr/bin/env python

import os
import subprocess
from abc import ABCMeta, abstractmethod
from pretty_printer import *

class CustomTaskManager(object):
    def __init__(self):
        self.tasks = list()

    def printMessages(self):
       for task in self.tasks:
           task.printHelpMessage()

    def doWorks(self):
        for task in self.tasks:
            task.doWork()

    def addTask(self, task):
        self.tasks.append(task)

class CustomTask(object):
    __metaclass__ = ABCMeta

    @classmethod
    def printHelpMessage(self): raise NotImplementedError

    @classmethod
    def doWork(self): raise NotImplementedError

class ZshTask(CustomTask):
    def __readStringFromCmd(self, cmd):
        ret_string = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).stdout.readline()
        if len(ret_string) == 0:
            return False
        return ret_string

    def printHelpMessage(self):
        printBlue("\t Default Zsh: change $SHELL config")

    def doWork(self):
        zsh_file_path = self.__readStringFromCmd("which zsh")
        if (zsh_file_path == False):
            printHeader("Can not find zsh installation")
        printHeader("Your new default shell path($SHELL): %s" % zsh_file_path)
        os.system("chsh -s %s" % zsh_file_path)

class VimColorTask(CustomTask):
    def printHelpMessage(self):
        printBlue("\t Jellybeans color: color for VIM")

    def doWork(self):
        os.system("mkdir -p ~/.vim/colors")
        os.system("cp ./custom_files/jellybeans.vim ~/.vim/colors/")

class VimVundleTask(CustomTask):
    def printHelpMessage(self):
        printBlue("\t Vundle: plugin framework for VIM")

    def doWork(self):
        os.system("mkdir -p ~/.vim/bundle")
        os.system("git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim")
        os.system("vim +PluginInstall +qall")

class GitConfigTask(CustomTask):
    def printHelpMessage(self):
        printBlue("\t Git: setting personal configuration for Git")

    def doWork(self):
        os.system('git config --global user.name "Jongmin Won"')
        os.system('git config --global user.email "operaun@gmail.com"')
        os.system('git config --global merge.tool vimdiff')
        os.system('git config --global core.editor vim')
        os.system('git config --global core.autocrlf false')
        os.system('git config --global core.filemode false')
        os.system('git config --global color.ui true')

