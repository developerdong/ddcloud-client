import os

import requests


class Storage:
    def __init__(self, workDir, server):
        self.workDir = workDir
        self.server = server

