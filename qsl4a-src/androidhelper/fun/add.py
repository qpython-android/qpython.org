#以下 SL4A函数 由 乘着船 添加

def videoPlay(self, path, wait=True):
    return self._rpc("videoPlay",path,wait)

def openFile(self, path, type=None, wait=True):
    return self._rpc("openFile",path,type,wait)

def sendFile(self, path, type=None, extras=None, wait=True):
    return self._rpc("sendFile",path,type,extras,wait)

def getApplicationInfo(self, packageName = None):
    return self._rpc("getApplicationInfo",packageName)

def recorderStartScreenRecord(self, path=None, audio=1, targetPixels=None, frameRate=30, bitRate=None, rotation=False, autoStart=True):
    return self._rpc("recorderStartScreenRecord",path,audio,targetPixels,frameRate,bitRate,rotation,autoStart)

def recorderPause(self):
    return self._rpc("recorderPause")

def recorderResume(self):
    return self._rpc("recorderResume")

def recorderStart(self):
    return self._rpc("recorderStart")

def imageReaderGetScreenShot(self, path = None, delayMilliSec = 1000):
    return self._rpc("imageReaderGetScreenShot",path,delayMilliSec)

def getMeid(self, slotIndex = None):
    return self._rpc("getMeid",slotIndex)

def getImei(self, slotIndex = None):
    return self._rpc("getImei",slotIndex)

def takePicture(self, path = None):
    return self._rpc("takePicture",path)

def takeVideo(self, path = None, quality = 1):
    return self._rpc("takeVideo",path,quality)

def recordAudio(self):
    return self._rpc("recordAudio")

def backgroundProtect(self, enabled = True):
    return self._rpc("backgroundProtect", enabled)

def recorderSoundVolumeDetect(self, interval = 100):
    return self._rpc('recorderSoundVolumeDetect',interval)

def recorderSoundVolumeGetDb(self):
    return self._rpc('recorderSoundVolumeGetDb')

def getLastLog(self,logFileName='last.log'):
    return self._rpc("getLastLog",logFileName)

def getLocale(self):
    return self._rpc("getLocale")

def getSysInfo(self):
    return self._rpc('getSysInfo')

def getAndroidID(self):
    return self._rpc('getAndroidID')

def getScreenInfo(self):
    return self._rpc('getScreenInfo')

def getMemoryInfo(self):
    return self._rpc('getMemoryInfo')

def createScriptShortCut(self,scriptPath,label=None,iconPath=None,scriptArg=None):
    return self._rpc('createScriptShortCut',scriptPath,label,iconPath,scriptArg)

def wifiGetApState(self):
    return self._rpc('wifiGetApState')

def getConnectedInfo(self):
    return self._rpc('getConnectedInfo')

def getDhcpInfo(self,ipConvertToString=True):
    return self._rpc('getDhcpInfo',ipConvertToString)

def getInstalledPackages(self, flag = 4):
    return self._rpc("getInstalledPackages",flag)

def getInternetInterfaceAddress(self):
    return self._rpc("getInternetInterfaceAddress")

def getTelephoneSignalStrengthDetail(self):
    return self._rpc("getTelephoneSignalStrengthDetail")

def getTelephoneSignalStrengthLevel(self):
    return self._rpc("getTelephoneSignalStrengthLevel")

def scanBarcodeFromImage(self, path, compressRatio = 0, x = 0, y = 0, width = 0, height = 0):
    return self._rpc("scanBarcodeFromImage",path, compressRatio, x, y, width, height)

def getHarmonyOsInformation(self):
    return self._rpc("getHarmonyOsInformation")

def isExternalStorageManager(self):
    return self._rpc("isExternalStorageManager")

def cameraCapturePicture(self, targetPath = None, cameraId = 0, useAutoFocus = True):
    return self._rpc("cameraCapturePicture",targetPath, cameraId, useAutoFocus)

def cameraSetTorchMode(self, enabled):
    return self._rpc("cameraSetTorchMode",enabled)

def recorderCaptureVideo(self, targetPath = None, duration = 10, cameraId = 0, quality = 8):
    return self._rpc("recorderCaptureVideo",targetPath, duration, cameraId, quality)

def getAllCellsLocation(self):
    return self._rpc("getAllCellsLocation")

def elapsedRealtimeNanos(self):
    return self._rpc("elapsedRealtimeNanos")

def sharedVariableSet(self, key, value):
    return self._rpc("sharedVariableSet", key, value)

def sharedVariableGet(self, key):
    return self._rpc("sharedVariableGet", key)

def sharedVariableRemove(self, key):
    return self._rpc("sharedVariableRemove", key)

def htmlPictureSetSize(self, widthFixed = None, heightFixed = None, widthRatio = None, heightRatio = None):
    return self._rpc("htmlPictureSetSize", widthFixed, heightFixed, widthRatio, heightRatio)

def htmlPictureGetSize(self):
    return self._rpc("htmlPictureGetSize")

def getFileStat(self, path):
    return self._rpc("getFileStat", path)

def getTrafficStats(self,flags=7):
    return self._rpc("getTrafficStats",flags)

def readGnssStatus(self):
    return self._rpc("readGnssStatus")

def prefRemoveValue(self,key,filename=None):
    return self._rpc("prefRemoveValue",key,filename)

def send(self,uri,type=None,extras=None,wait=True):
    return self._rpc("send",uri,type,extras,wait)

def sendText(self,text,extras=None,wait=True):
    return self._rpc("sendText",text,extras,wait)

def showScreenLock(self):
    return self._rpc("showScreenLock")

def checkPermissions(self):
    return self._rpc('checkPermissions')

def requestPermissions(self, permissions = None):
    return self._rpc('requestPermissions', permissions)

def ttsStop(self):
    return self._rpc("ttsStop")

def getSdCardPaths(self):
    return self._rpc("getSdCardPaths")

def imageCompress(self,srcPath,destPath,targetByteSize=0,targetWidth=0,targetHeight=0):
    return self._rpc("imageCompress",srcPath,destPath,targetByteSize,targetWidth,targetHeight)

def editorOpen(self, path):
    return self._rpc("editorOpen", path)