import os

import requests


class Storage:
    def __init__(self, workDir, server):
        self.workDir = workDir
        self.server = server

    def getAbsolutePath(self, path):
        os.path.join(self.workDir, path)

    def cd(self, dirPath):
        if dirPath is not '.':
            if dirPath is '..':
                if self.workDir is not '/':
                    self.workDir = os.path.dirname(self.workDir)
            elif os.path.isabs(dirPath):
                self.workDir = dirPath
            else:
                self.workDir = os.path.join(self.workDir, dirPath)

    def mkdir(self, dirPath):
        response = requests.post(self.server + '/file/createDir', {'dirPath', self.getAbsolutePath(dirPath)})
        return response.json()

    def ls(self, dirPath):
        response = requests.post(self.server + '/file/list', {'dirPath', self.getAbsolutePath(dirPath)})
        return response.json()

    def upload(self, localFilePath, destDirPath):
        if os.path.exists(localFilePath) and not os.path.isdir(localFilePath):
            response = requests.post(self.server + '/file/upload', {'destDirPath', self.getAbsolutePath(destDirPath)}, files={'file': open(localFilePath, 'rb')})
            return response.json()
        else:
            print('本地文件不存在，请检查路径')
