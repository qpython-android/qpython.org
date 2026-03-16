def environment(self):
    return self._rpc("environment")

def getClipboard(self):
    return self._rpc("getClipboard")

def getConstants(self,classname):
    return self._rpc("getConstants",classname)

def getIntent(self):
    return self._rpc("getIntent")

def getPackageVersion(self,packageName):
    return self._rpc("getPackageVersion",packageName)

def getPackageVersionCode(self,packageName):
    return self._rpc("getPackageVersionCode",packageName)

def log(self,message):
    return self._rpc("log",message)

def sendBroadcastIntent(self,intent):
    return self._rpc("sendBroadcastIntent",intent)

def setClipboard(self,text):
    return self._rpc("setClipboard",text)

def startActivityForResultIntent(self,intent):
    return self._rpc("startActivityForResultIntent",intent)

def startActivityIntent(self,intent,wait=None):
    return self._rpc("startActivityIntent",intent,wait)

def vibrate(self,duration=300):
    return self._rpc("vibrate",duration)

def forceStopPackage(self,packageName):
    return self._rpc("forceStopPackage",packageName)

def getRunningPackages(self):
    return self._rpc("getRunningPackages")

def pick(self,uri):
    return self._rpc("pick",uri)

def search(self,query):
    return self._rpc("search",query)

def contactsGet(self,attributes=None):
    return self._rpc("contactsGet",attributes)

def contactsGetAttributes(self):
    return self._rpc("contactsGetAttributes")

def contactsGetById(self,id,attributes=None):
    return self._rpc("contactsGetById",id,attributes)

def contactsGetCount(self):
    return self._rpc("contactsGetCount")

def contactsGetIds(self):
    return self._rpc("contactsGetIds")

def pickContact(self):
    return self._rpc("pickContact")

def pickPhone(self):
    return self._rpc("pickPhone")

def queryAttributes(self,uri):
    return self._rpc("queryAttributes",uri)

def queryContent(self,uri,attributes=None,selection=None,selectionArgs=None,order=None):
    return self._rpc("queryContent",uri,attributes,selection,selectionArgs,order)

def eventClearBuffer(self):
    return self._rpc("eventClearBuffer")

def eventGetBrodcastCategories(self):
    return self._rpc("eventGetBrodcastCategories")

def eventPoll(self,number_of_events=1):
    return self._rpc("eventPoll",number_of_events)

def eventPost(self,name,data,enqueue=None):
    return self._rpc("eventPost",name,data,enqueue)

def eventRegisterForBroadcast(self,category,enqueue=True):
    return self._rpc("eventRegisterForBroadcast",category,enqueue)

def eventUnregisterForBroadcast(self,category):
    return self._rpc("eventUnregisterForBroadcast",category)

def eventWait(self,timeout=None):
    return self._rpc("eventWait",timeout)

def eventWaitFor(self,eventName,timeout=None):
    return self._rpc("eventWaitFor",eventName,timeout)

def receiveEvent(self):
    return self._rpc("receiveEvent")

def rpcPostEvent(self,name,data):
    return self._rpc("rpcPostEvent",name,data)

def startEventDispatcher(self,port=None):
    return self._rpc("startEventDispatcher",port)

def stopEventDispatcher(self):
    return self._rpc("stopEventDispatcher")

def waitForEvent(self,eventName,timeout=None):
    return self._rpc("waitForEvent",eventName,timeout)

def geocode(self,latitude,longitude,maxResults=1):
    return self._rpc("geocode",latitude,longitude,maxResults)

def getLastKnownLocation(self):
    return self._rpc("getLastKnownLocation")

def readLocation(self):
    return self._rpc("readLocation")

def stopLocating(self):
    return self._rpc("stopLocating")

def mediaIsPlaying(self,tag="default"):
    return self._rpc("mediaIsPlaying",tag)

def mediaPlay(self,url,tag="default",play=True):
    return self._rpc("mediaPlay",url,tag,play)

def mediaPlayClose(self,tag="default"):
    return self._rpc("mediaPlayClose",tag)

def mediaPlayInfo(self,tag="default"):
    return self._rpc("mediaPlayInfo",tag)

def mediaPlayList(self):
    return self._rpc("mediaPlayList")

def mediaPlayPause(self,tag="default"):
    return self._rpc("mediaPlayPause",tag)

def mediaPlaySeek(self,msec,tag="default"):
    return self._rpc("mediaPlaySeek",msec,tag)

def mediaPlaySetLooping(self,enabled=True,tag="default"):
    return self._rpc("mediaPlaySetLooping",enabled,tag)

def mediaPlayStart(self,tag="default"):
    return self._rpc("mediaPlayStart",tag)

def recorderStop(self):
    return self._rpc("recorderStop")

def checkNetworkRoaming(self):
    return self._rpc("checkNetworkRoaming")

def getDeviceSoftwareVersion(self):
    return self._rpc("getDeviceSoftwareVersion")

def getLine1Number(self):
    return self._rpc("getLine1Number")

def getAllCellInfo(self):
    return self._rpc("getAllCellInfo")

def getNetworkOperator(self):
    return self._rpc("getNetworkOperator")

def getNetworkOperatorName(self):
    return self._rpc("getNetworkOperatorName")

def getNetworkType(self):
    return self._rpc("getNetworkType")

def getPhoneType(self):
    return self._rpc("getPhoneType")

def getSimCountryIso(self):
    return self._rpc("getSimCountryIso")

def getSimOperator(self):
    return self._rpc("getSimOperator")

def getSimOperatorName(self):
    return self._rpc("getSimOperatorName")

def getSimSerialNumber(self):
    return self._rpc("getSimSerialNumber")

def getSimState(self):
    return self._rpc("getSimState")

def getSubscriberId(self):
    return self._rpc("getSubscriberId")

def getVoiceMailAlphaTag(self):
    return self._rpc("getVoiceMailAlphaTag")

def getVoiceMailNumber(self):
    return self._rpc("getVoiceMailNumber")

def phoneCall(self,uri):
    return self._rpc("phoneCall",uri)

def phoneCallNumber(self,phone_number):
    return self._rpc("phoneCallNumber",phone_number)

def phoneDial(self,uri):
    return self._rpc("phoneDial",uri)

def phoneDialNumber(self,phone_number):
    return self._rpc("phoneDialNumber",phone_number)

def readPhoneState(self):
    return self._rpc("readPhoneState")

def startTrackingPhoneState(self):
    return self._rpc("startTrackingPhoneState")

def stopTrackingPhoneState(self):
    return self._rpc("stopTrackingPhoneState")

def prefGetAll(self,filename=None):
    return self._rpc("prefGetAll",filename)

def prefGetValue(self,key,filename=None):
    return self._rpc("prefGetValue",key,filename)

def prefPutValue(self,key,value,filename=None):
    return self._rpc("prefPutValue",key,value,filename)

def stopSensing(self):
    return self._rpc("stopSensing")

def checkAirplaneMode(self):
    return self._rpc("checkAirplaneMode")

def checkRingerSilentMode(self):
    return self._rpc("checkRingerSilentMode")

def checkScreenOn(self):
    return self._rpc("checkScreenOn")

def getMaxMediaVolume(self):
    return self._rpc("getMaxMediaVolume")

def getMaxRingerVolume(self):
    return self._rpc("getMaxRingerVolume")

def getMediaVolume(self):
    return self._rpc("getMediaVolume")

def getRingerVolume(self):
    return self._rpc("getRingerVolume")

def getScreenBrightness(self):
    return self._rpc("getScreenBrightness")

def getScreenTimeout(self):
    return self._rpc("getScreenTimeout")

def getVibrateMode(self,ringer=None):
    return self._rpc("getVibrateMode",ringer)

def setMediaVolume(self,volume):
    return self._rpc("setMediaVolume",volume)

def setRingerVolume(self,volume):
    return self._rpc("setRingerVolume",volume)

def setScreenTimeout(self,value):
    return self._rpc("setScreenTimeout",value)

#def toggleAirplaneMode(self,enabled=None):
#    return self._rpc("toggleAirplaneMode",enabled)

def toggleRingerSilentMode(self,enabled=None):
    return self._rpc("toggleRingerSilentMode",enabled)

def toggleVibrateMode(self,enabled=None,ringer=None):
    return self._rpc("toggleVibrateMode",enabled,ringer)

def readSignalStrengths(self):
    return self._rpc("readSignalStrengths")

def startTrackingSignalStrengths(self):
    return self._rpc("startTrackingSignalStrengths")

def stopTrackingSignalStrengths(self):
    return self._rpc("stopTrackingSignalStrengths")

def smsDeleteMessage(self,id):
    return self._rpc("smsDeleteMessage",id)

def smsGetAttributes(self):
    return self._rpc("smsGetAttributes")

def smsGetMessageById(self,id,attributes=None):
    return self._rpc("smsGetMessageById",id,attributes)

def smsGetMessageCount(self,unreadOnly,folder="inbox"):
    return self._rpc("smsGetMessageCount",unreadOnly,folder)

def smsGetMessageIds(self,unreadOnly,folder="inbox"):
    return self._rpc("smsGetMessageIds",unreadOnly,folder)

def smsGetMessages(self,unreadOnly,folder="inbox",attributes=None):
    return self._rpc("smsGetMessages",unreadOnly,folder,attributes)

def smsMarkMessageRead(self,ids,read):
    return self._rpc("smsMarkMessageRead",ids,read)

def ttsIsSpeaking(self):
    return self._rpc("ttsIsSpeaking")

def generateDtmfTones(self,phoneNumber,toneDuration=100):
    return self._rpc("generateDtmfTones",phoneNumber,toneDuration)

def wakeLockAcquireBright(self):
    return self._rpc("wakeLockAcquireBright")

def wakeLockAcquireDim(self):
    return self._rpc("wakeLockAcquireDim")

def wakeLockAcquireFull(self):
    return self._rpc("wakeLockAcquireFull")

def wakeLockAcquirePartial(self):
    return self._rpc("wakeLockAcquirePartial")

def wakeLockRelease(self):
    return self._rpc("wakeLockRelease")

def cameraStartPreview(self,resolutionLevel=0,jpegQuality=20,filepath=None):
    return self._rpc("cameraStartPreview",resolutionLevel,jpegQuality,filepath)

def cameraStopPreview(self):
    return self._rpc("cameraStopPreview")

def webcamAdjustQuality(self,resolutionLevel=0,jpegQuality=20):
    return self._rpc("webcamAdjustQuality",resolutionLevel,jpegQuality)

def webcamStart(self,resolutionLevel=0,jpegQuality=20,port=0):
    return self._rpc("webcamStart",resolutionLevel,jpegQuality,port)

def webcamStop(self):
    return self._rpc("webcamStop")

def checkWifiState(self):
    return self._rpc("checkWifiState")

def toggleWifiState(self,enabled=None):
    return self._rpc("toggleWifiState",enabled)

def wifiDisconnect(self):
    return self._rpc("wifiDisconnect")

def wifiGetConnectionInfo(self):
    return self._rpc("wifiGetConnectionInfo")

def wifiGetScanResults(self):
    return self._rpc("wifiGetScanResults")

def wifiLockAcquireFull(self):
    return self._rpc("wifiLockAcquireFull")

def wifiLockAcquireScanOnly(self):
    return self._rpc("wifiLockAcquireScanOnly")

def wifiLockRelease(self):
    return self._rpc("wifiLockRelease")

def wifiReassociate(self):
    return self._rpc("wifiReassociate")

def wifiReconnect(self):
    return self._rpc("wifiReconnect")

def wifiStartScan(self):
    return self._rpc("wifiStartScan")
