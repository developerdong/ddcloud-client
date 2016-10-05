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
    if cmd is None or cmd == 'help':
        pass
    elif cmd == 'ls':
        pass
    elif cmd == 'cd':
        pass
    elif cmd == 'mkdir':
        pass
    elif cmd == 'up':
        pass
    elif cmd == 'down':
        pass
    elif cmd == 're':
        pass
    elif cmd == 'mv':
        pass
    elif cmd == 'rm':
        pass
    elif cmd == 'signup':
        pass
    elif cmd == 'login':
        pass
    elif cmd == 'logout':
        pass

INIT_WORK_DIR = '/'
SERVER = 'http://localhost:8080'

interface = ServerInterface(INIT_WORK_DIR, SERVER)
while True:
    args = str(input()).split()
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
        result = interface.cd(args[1])
    elif args[0] == 'mkdir':
        result = interface.mkdir(args[1])
    elif args[0] == 'up':
        result = interface.up(args[1], args[2])
    elif args[0] == 'down':
        result = interface.down(args[1], args[2])
    elif args[0] == 're':
        result = interface.re(args[1], args[2])
    elif args[0] == 'mv':
        result = interface.mv(args[1], args[2])
    elif args[0] == 'rm':
        result = interface.mv(args[1], args[2])
    elif args[0] == 'signup':
        result = interface.signup(args[1], args[2])
    elif args[0] == 'login':
        result = interface.login(args[1], args[2])
    elif args[0] == 'logout':
        result = interface.logout()
    elif args[0] == 'exit':
        break
    elif args[0] == 'help':
        printHelp()
    else:
        printHelp()
