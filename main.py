from ServerInterface import ServerInterface


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
        result = interface.ls(args[1])
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
