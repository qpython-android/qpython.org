_doc_='''readSensors()
Returns the most recently recorded sensor data.

sensorsGetAccuracy()
Returns the most recently received accuracy value.

sensorsGetLight()
Returns the most recently received light value.

sensorsGetStepCounter()
Returns the most recently Step Counter.

sensorsReadGyroscope()
Returns the most recently received gyroscope value.

sensorsReadAccelerometer()
Returns the most recently received accelerometer values.
returns: (List) a List of Floats [(acceleration on the) X axis, Y axis, Z axis].

sensorsReadMagnetometer()
Returns the most recently received magnetic field values.
returns: (List) a List of Floats [(magnetic field value for) X axis, Y axis, Z axis].

sensorsReadOrientation()
Returns the most recently received orientation values.
returns: (List) a List of Doubles [azimuth, pitch, roll].

stopSensing()
Stops collecting sensor data.'''

_g=_doc_.split('\n\n')

for _t in _g:
    _i=_t[:_t.find('(')]
    exec(f'''
def {_i}(self):
    return self._rpc("{_i}")
{_i}.__doc__=_t
''')

def startSensingThreshold(self,sensorNumber,threshold,axis):
    return self._rpc("startSensingThreshold",sensorNumber,threshold,axis)

def startSensingTimed(self,sensorNumber,delayTime):
    return self._rpc("startSensingTimed",sensorNumber,delayTime)

_g='\n\n'
for _i in ('startSensingTimed','startSensingThreshold'):
    exec(f'{_i}.__doc__=_self.{_i}.__doc__')
    exec(eval(f'{_i}.__doc__.rsplit(_g,1)[1]'))

del _g,_i,_t,_doc_