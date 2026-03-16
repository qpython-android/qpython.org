#以下 SL4A函数 由 Xmile 修复

def usbserialGetDeviceList(self):
    return self._rpc("usbserialGetDeviceList")

def usbserialDisconnect(self, connID = ""):
    return self._rpc("usbserialDisconnect", connID)

def usbserialConnect(self, hash = "", options =""):
    return self._rpc("usbserialConnect", hash, options)

def usbserialWrite(self, ascii, connID = ""):
    return self._rpc("usbserialWrite", ascii, connID)

def usbserialReadReady(self, connID = ""):
    return self._rpc("usbserialReadReady", connID)

def usbserialRead(self, connID = "", bufferSize = 4096):
    return self._rpc("usbserialRead", connID, bufferSize)
