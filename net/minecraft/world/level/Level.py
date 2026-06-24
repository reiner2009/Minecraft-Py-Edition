isClient = False
isServer = False

def setEnv(env):
    global isClient
    global isServer
    if env=="client" and not isServer:
        isClient = True
    elif env=="server" and not isClient:
        isServer = True