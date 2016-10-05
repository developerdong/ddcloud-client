import math

from datetime import datetime
from prettytable import PrettyTable

from ServerInterface import ServerInterface


def convertBytes(length, lst=('Bytes', 'KB', 'MB', 'GB', 'TB', 'PB')):
    index = 0 if length == 0 else int(math.floor(math.log(length, 1024)))
    if index >= len(lst):
        index = len(lst) - 1
    return ('%.2f' + " " + lst[index]) % (length / math.pow(1024, index))


def printHelp(cmd=None):
    helpTable = PrettyTable(['命令', '参数1', '参数2', '描述'])
    if cmd == 'ls':
        helpTable.add_row(['ls', 'dirPath', '空', '显示文件列表，默认显示当前工作目录'])
    elif cmd == 'cd':
        helpTable.add_row(['cd', 'dirPath', '空', '切换当前工作目录'])
    elif cmd == 'mkdir':
        helpTable.add_row(['mkdir', 'dirPath', '空', '创建目录'])
    elif cmd == 'up':
        helpTable.add_row(['up', 'localFilePath', 'destDirPath', '将本地文件上传到云盘中某一目录'])
    elif cmd == 'down':
        helpTable.add_row(['down', 'filePath', 'localFilePath', '将云盘文件保存为本地某一文件'])
    elif cmd == 're':
        helpTable.add_row(['re', 'oldPath', 'newPath', '重命名文件或目录'])
    elif cmd == 'mv':
        helpTable.add_row(['mv', 'oldPath', 'newPath', '移动文件或目录'])
    elif cmd == 'rm':
        helpTable.add_row(['rm', 'path', '空', '永久删除文件或目录'])
    elif cmd == 'signup':
        helpTable.add_row(['signup', 'username', 'password', '注册新用户'])
    elif cmd == 'login':
        helpTable.add_row(['login', 'username', 'password', '登录'])
    elif cmd == 'logout':
        helpTable.add_row(['logout', '空', '空', '注销'])
    else:
        helpTable.add_row(['help', '空', '空', '查看帮助'])
        helpTable.add_row(['ls', '[dirPath]', '空', '显示文件列表，默认显示当前工作目录'])
        helpTable.add_row(['cd', 'dirPath', '空', '切换当前工作目录'])
        helpTable.add_row(['mkdir', 'dirPath', '空', '创建目录'])
        helpTable.add_row(['up', 'localFilePath', 'destDirPath', '将本地文件上传到云盘中某一目录'])
        helpTable.add_row(['down', 'filePath', 'localFilePath', '将云盘文件保存为本地某一文件'])
        helpTable.add_row(['re', 'oldPath', 'newPath', '重命名文件或目录'])
        helpTable.add_row(['mv', 'oldPath', 'newPath', '移动文件或目录'])
        helpTable.add_row(['rm', 'path', '空', '永久删除文件或目录'])
        helpTable.add_row(['signup', 'username', 'password', '注册新用户'])
        helpTable.add_row(['login', 'username', 'password', '登录'])
        helpTable.add_row(['logout', '空', '空', '注销'])
        helpTable.add_row(['exit', '空', '空', '退出程序'])
    print(helpTable)

INIT_WORK_DIR = '/'
SERVER = 'http://localhost:8080'

interface = ServerInterface(INIT_WORK_DIR, SERVER)
while True:
    args = str(input()).split()
    if len(args) == 0:
        continue
    if args[0] == 'ls':
        if len(args) == 1 or len(args) == 2:
            result = interface.ls(args[1] if len(args) == 2 else None)
            if result is not None:
                if result['status'] == 200:
                    fileTable = PrettyTable(['序号', '名称', '大小', '目录', '修改时间', '访问时间'])
                    for i, row in enumerate(result['result']):
                        fileTable.add_row([i, row['name'], convertBytes(row['length']), row['dir'],
                                           datetime.fromtimestamp(row['modificationTime'] / 1000),
                                           datetime.fromtimestamp(row['accessTime'] / 1000)])
                    print(fileTable)
                else:
                    print(result['result'])
        else:
            printHelp('ls')
    elif args[0] == 'cd':
        if len(args) == 2:
            interface.cd(args[1])
        else:
            printHelp('cd')
    elif args[0] == 'mkdir':
        if len(args) == 2:
            print(interface.mkdir(args[1])['result'])
        else:
            printHelp('mkdir')
    elif args[0] == 'up':
        if len(args) == 3:
            result = interface.up(args[1], args[2])
            if result is not None:
                print(result['result'])
        else:
            printHelp('up')
    elif args[0] == 'down':
        if len(args) == 3:
            result = interface.down(args[1], args[2])
            if result is not None:
                print(result['result'])
        else:
            printHelp('down')
    elif args[0] == 're':
        if len(args) == 3:
            print(interface.re(args[1], args[2])['result'])
        else:
            printHelp('re')
    elif args[0] == 'mv':
        if len(args) == 3:
            print(interface.mv(args[1], args[2])['result'])
        else:
            printHelp('mv')
    elif args[0] == 'rm':
        if len(args) == 2:
            print(interface.rm(args[1])['result'])
        else:
            printHelp('rm')
    elif args[0] == 'signup':
        if len(args) == 3:
            print(interface.signup(args[1], args[2])['result'])
        else:
            printHelp('signup')
    elif args[0] == 'login':
        if len(args) == 3:
            print(interface.login(args[1], args[2])['result'])
        else:
            printHelp('login')
    elif args[0] == 'logout':
        if len(args) == 1:
            print(interface.logout()['result'])
        else:
            printHelp('logout')
    elif args[0] == 'exit':
        break
    elif args[0] == 'help':
        printHelp()
    else:
        printHelp()
