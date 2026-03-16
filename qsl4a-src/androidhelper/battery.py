_doc_='''batteryStartMonitoring()

batteryStopMonitoring()
Stops tracking battery state.

batteryCheckPresent()
Returns the most recently received battery presence data.

batteryGetHealth()
Returns the most recently received battery health data:1 - unknown;2 - good;3 - overheat;4 - dead;5 - over voltage;6 - unspecified failure;

batteryGetLevel()
Returns the most recently received battery level (percentage).

batteryGetPlugType()
Returns the most recently received plug type data:
-1 - unknown;
0 - unplugged;
1 - power source is an AC charger;
2 - power source is a USB port

batteryGetStatus()
Returns  the most recently received battery status data:1 - unknown;2 - charging;3 - discharging;4 - not charging;5 - full;

batteryGetTechnology()
Returns the most recently received battery technology data.

batteryGetTemperature()
Returns the most recently received battery temperature.

batteryGetVoltage()
Returns the most recently received battery voltage mV .

readBatteryData()
Returns the most recently recorded battery data.

batteryGetCurrent()
Returns the most recently received battery Current mA .

batteryGetCharge()
Returns the most recently received battery Charge Counter μAh .
'''

_g=_doc_.split('\n\n')

for _t in _g:
	_i=_t[:_t.find('(')]
	exec(f'def {_i}(self):return self._rpc("{_i}")')
	if _t.find('\n')==-1:
	    _t=eval(f'_self.{_i}.__doc__')
	exec(f"{_i}.__doc__=_t")

del _g,_i,_t,_doc_
