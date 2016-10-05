#!/usr/bin/env python

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
