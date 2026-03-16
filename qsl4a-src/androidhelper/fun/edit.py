#以下 SL4A函数 被 乘着船 修改

def makeToast(self,message,length=0,isHtml=False,backColor=None,textColor=None,textSize=0,textAlign=0):
    return self._rpc("makeToast",message,length,isHtml,backColor,textColor,textSize,textAlign)

def notify(self, title, message, uri=None, arg=None):
    return self._rpc("notify",title,message,uri,arg)

def getLaunchablePackages(self,needClassName=False):
    return self._rpc("getLaunchablePackages",needClassName)

def launch(self,classname=None,packagename=None,wait=True):
    return self._rpc("launch",classname,packagename,wait)

def view(self,uri,type=None,extras=None,wait=True):
    return self._rpc("view",uri,type,extras,wait)

def viewContacts(self,wait=True):
    return self._rpc("viewContacts",wait)

def viewMap(self,query,wait=True):
    return self._rpc("viewMap",query,wait)

def scanBarcode(self, title = None):
    return self._rpc("scanBarcode",title)

def getCellLocation(self):
    return self._rpc("getCellLocation")

def recorderStartMicrophone(self,targetPath=None):
    return self._rpc("recorderStartMicrophone",targetPath)

def smsSend(self,destinationAddress,text):
    return self._rpc("smsSend",destinationAddress,text)

def viewHtml(self,path,title=None,wait=True):
    return self._rpc("viewHtml",path,title,wait)
webViewShow=viewHtml

def executeQPy(self,scriptPath='',arg=None):
    return self._rpc("executeQPy",scriptPath,arg)

def startLocating(self,minUpdateTime=60000,minUpdateDistance=30,updateGnssStatus=False):
    return self._rpc("startLocating",minUpdateTime,minUpdateDistance,updateGnssStatus)

def setScreenBrightness(self,value=None):
    return self._rpc("setScreenBrightness",value)

def ttsSpeak(self,message,pitch=1,pitchRate=1):
    return self._rpc("ttsSpeak",message,pitch,pitchRate)

def sendEmail(self,to,subject,text,attachmentPath=None,extras=None,wait=True):
    return self._rpc("sendEmail",to,subject,text,attachmentPath,extras,wait)

def startActivity(self,action,uri=None,type=None,extras=None,wait=None,packagename=None,classname=None,flags=None):
    return self._rpc("startActivity",action,uri,type,extras,wait,packagename,classname,flags)

def startActivityForResult(self,action,uri=None,type=None,extras=None,packagename=None,classname=None,flags=None):
    return self._rpc("startActivityForResult",action,uri,type,extras,packagename,classname,flags)

def sendBroadcast(self,action,uri=None,type=None,extras=None,packagename=None,classname=None,flags=None):
    return self._rpc("sendBroadcast",action,uri,type,extras,packagename,classname,flags)
