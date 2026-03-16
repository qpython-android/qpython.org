#add Method

def batteryStartMonitoring(self):
    self._addMethod('battery')
    return self.batteryStartMonitoring()

def startSensingThreshold(self,sensorNumber,threshold,axis):
    self._addMethod('sensor')
    return self.startSensingThreshold(sensorNumber,threshold,axis)

def startSensingTimed(self,sensorNumber,delayTime):
    self._addMethod('sensor')
    return self.startSensingTimed(sensorNumber,delayTime)

def checkBluetoothState(self):
    self._addMethod('bluetooth')
    return self.checkBluetoothState()

def toggleBluetoothState(self,enabled=None,prompt=True):
    self._addMethod('bluetooth')
    return self.toggleBluetoothState(enabled,prompt)

_addMethod('accessibility')
_addMethod('floatView/__init__')

#add Class

def cipherInit( self, key, algorithm = "AES/CBC/PKCS5Padding", encodingFormat = "", initialVector = "" ):
    self._addClass('cipher')
    return self.cipherInit( key, algorithm, encodingFormat, initialVector )

def documentTreeShowOpen( self, rootPath='/sdcard' ):
    self._addClass('documentFile')
    return self.documentTreeShowOpen( rootPath )

def speechToText(self, RecordSecond = 10, AmrFile = None, Language = None):
    self._addClass('pgptai')
    return self.speechToText(RecordSecond, AmrFile, Language)

def textToSpeech(self, Text, AutoPlay = True, WavFile = None, VoiceName = None):
    self._addClass('pgptai')
    return self.textToSpeech(Text, AutoPlay, WavFile, VoiceName)

def notebookOpen(self, path = None):
    os = sl4a.os
    npy = os.environ["HOME"]+"/bin/NoteBook.py"
    if path:
        return self._rpc("executeQPy", npy, os.path.abspath(path))
    return self._rpc("executeQPy", npy)

#add Constant

@property
def R(self):
    from . import R
    R=R.R()
    Android.R=R
    return R

@property
def provider(self):
    from . import provider as p
    p=p.provider()
    Android.provider=p
    return p

@property
def Intent(self):
    from . import Intent as i
    Android.Intent=i
    return i
