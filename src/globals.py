#!/usr/bin/env python
# Copyright (C) 2019 Roshan Lamichhane

import os

globals = None

class _Globals:
    def __init__(self):
        self.appName = 'RoshanDrop'
        self.version = '0.0.1'
        self.roshandrop = None
        self.baseDir = None
        self.confDir = os.path.join(os.path.expanduser('~'), '.' + self.appName)
        self.cfgFile = os.path.join(self.confDir, 'config.ini')
        self.cfgDb = os.path.join(self.confDir, 'config.db')
        self.logFile = os.path.join(self.confDir, 'pythondrop.log')
        self.config = None
        self.argv = None

        self.DEFAULT_CONFIG = ""

def Globals():
    global globals
    if not globals:
        globals = _Globals()
    return globals
