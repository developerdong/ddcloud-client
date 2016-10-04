import os

import requests


class ServerInterface:
    def __init__(self, workDir, server, token):
        self.workDir = workDir
        self.server = server
        self.token = token

    def getAbsolutePath(self, path):
        return os.path.join(self.workDir, path)

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
        response = requests.post(self.server + '/file/createDir',
                                 {'dirPath': self.getAbsolutePath(dirPath), 'token': self.token})
        return response.json()

    def ls(self, dirPath):
        response = requests.post(self.server + '/file/list',
                                 {'dirPath': self.getAbsolutePath(dirPath), 'token': self.token})
        return response.json()

    def up(self, localFilePath, destDirPath):
        if os.path.exists(localFilePath) and not os.path.isdir(localFilePath):
            response = requests.post(self.server + '/file/upload',
                                     {'destDirPath': self.getAbsolutePath(destDirPath), 'token': self.token},
                                     files={'file': open(localFilePath, 'rb')})
            return response.json()
        else:
            print('本地文件不存在，请检查路径')

    def down(self, localFilePath, filePath):
        if not os.path.exists(localFilePath):
            response = requests.post(self.server + '/file/download',
                                     {'filePath': self.getAbsolutePath(filePath), 'token': self.token})
            if str(response.headers['Content-Type']).find('application/json') == -1:
                with open(localFilePath, 'wb') as f:
                    f.write(response.content)
            else:
                return response.json()
        else:
            print('本地文件已存在，请检查路径')

    def re(self, oldPath, newPath):
        response = requests.post(self.server + '/file/rename',
                                 {'oldPath': self.getAbsolutePath(oldPath), 'newPath': self.getAbsolutePath(newPath),
                                  'token': self.token})
        return response.json()

    def mv(self, oldPath, newPath):
        response = requests.post(self.server + '/file/move',
                                 {'oldPath': self.getAbsolutePath(oldPath), 'newPath': self.getAbsolutePath(newPath),
                                  'token': self.token})
        return response.json()

    def rm(self, path):
        response = requests.post(self.server + '/file/delete',
                                 {'path': self.getAbsolutePath(path), 'token': self.token})
        return response.json()

    def signup(self, username, password):
        response = requests.post(self.server + '/user/signup', {'username': username, 'password': password})
        return response.json()

    def login(self, username, password):
        response = requests.post(self.server + '/user/login', {'username': username, 'password': password})
        result = response.json()
        if result['status'] == 200:
            self.token = result['token']
        return result

    def logout(self):
        response = requests.post(self.server + '/user/logout', {'token': self.token})
        return response.json()
