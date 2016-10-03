import os

import requests


class Storage:
    def __init__(self, workDir, server):
        self.workDir = workDir
        self.server = server

    def getAbsolutePath(self, path):
        os.path.join(self.workDir, path)

