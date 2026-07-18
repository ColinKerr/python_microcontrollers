from irrecvdata import irGetCMD

def commandHandler(hexValue):
    print(hex(hexValue))

recvPin = irGetCMD(21, commandHandler)