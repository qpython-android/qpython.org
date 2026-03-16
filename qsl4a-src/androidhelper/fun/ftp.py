#以下 SL4A函数 由 乘着船 添加

def ftpGet(self):
    return self._rpc("ftpGet")

def ftpSet(self, port = None, rootDir = None, username = None, password = None):
    return self._rpc("ftpSet", port, rootDir, username, password)

def ftpStart(self):
    return self._rpc("ftpStart")

def ftpStop(self):
    return self._rpc("ftpStop")

def ftpIsRunning(self):
    return self._rpc("ftpIsRunning")

def ftpStatus(self):
    return self._rpc("ftpStatus")