_d='''    Include fields are name, bondState, type, uuid, connected, battery (if connected)  .
    type : 0 = Unknown , 1 = Classic , 2 = LowEnergy , 3 = Dual .'''
_d=f'''
Accept(uuid="457807c0-4897-11df-9879-0800200c9a66",timeout=0)
Listens for and accepts a Bluetooth connection. Blocks until the connection is established or fails.
    uuid (String)  (default=457807c0-4897-11df-9879-0800200c9a66)
    timeout (Integer) How long to wait for a new connection, 0 is wait for ever (default=0)

ActiveConnections()
Returns true when there's an active Bluetooth connection.

Connect(uuid="457807c0-4897-11df-9879-0800200c9a66",address=None)
Connect to a device over Bluetooth. Blocks until the connection is established or fails.
    uuid (String) The UUID passed here must match the UUID used by the server device. (default=457807c0-4897-11df-9879-0800200c9a66)
    address (String) The user will be presented with a list of discovered devices to choose from if an address is not provided. (optional)
returns: (String) True if the connection was established successfully.

GetConnectedDeviceName(connID=None)
Returns the name of the connected device.
    connID (String) Connection id (optional) (default=)

GetLocalName()
Gets the Bluetooth Visible device name

GetRemoteDeviceName(address)
Queries a remote device for it's name or null if it can't be resolved
    address (String) Bluetooth Address For Target Device

GetScanMode()
Gets the scan mode for the local dongle.
Return values:
    -1 when Bluetooth is disabled.
    0 if non discoverable and non connectable.
    1 connectable non discoverable.
    3 connectable and discoverable.

MakeDiscoverable(duration=300)
Requests that the device be discoverable for Bluetooth connections.
    duration (Integer) period of time, in seconds, during which the device should be discoverable (default=300)

Read(bufferSize=4096,connID=None)
Read up to bufferSize ASCII characters.
    bufferSize (Integer)  (default=4096)
    connID (String) Connection id (optional) (default=)

ReadBinary(bufferSize=4096,connID=None)
Read up to bufferSize bytes and return a chunked, base64 encoded string.
    bufferSize (Integer)  (default=4096)
    connID (String) Connection id (optional) (default=)

ReadLine(connID=None)
Read the next line.
    connID (String) Connection id (optional) (default=)

ReadReady(connID=None)
Returns True if the next read is guaranteed not to block.
    connID (String) Connection id (optional) (default=)

SetLocalName(name)
Sets the Bluetooth Visible device name, returns True on success
    name (String) New local name

Stop(connID=None)
Stops Bluetooth connection.
    connID (String) Connection id (optional) (default=)

Write(ascii,connID="")
Sends ASCII characters over the currently open Bluetooth connection.
    ascii (String)
    connID (String) Connection id (default=)

WriteBinary(base64,connID=None)
Send bytes over the currently open Bluetooth connection.
    base64 (String) A base64 encoded String of the bytes to be sent.
    connID (String) Connection id (optional) (default=)

checkBluetoothState()

toggleBluetoothState(enabled=None,prompt=True)

DiscoveryStart()
    Start Bluetooth Discovery

DiscoveryCancel()
    Cancel Bluetooth Discovery

GetReceivedDevices()
    Get received Bluetooth devices after droid.bluetoothDiscoveryStart() function
{_d}

GetBondedDevices()
    Get bonded devices , with address,name,type,bondState,uuid .
    You need to open Bluetooth with droid.toggleBluetoothState(True) .
    If you call droid.bluetoothGetBondedDevicesRssi(interval) with interval>0 first , it will return rssi of connected device at the same time .
{_d}

GetBondedDevicesRssi(interval=None)
  interval (Integer Optional)
    If interval > 0 , start detect connected devices' Rssi,
    if interval < 0 , stop detect connected devices' Rssi,
    if interval == 0 or interval == None , return connected device's address and Rssi, or return unconnected devices' address , you need to call droid.bluetoothGetBondedDevicesRssi(interval) with interval>0 first .
'''

for _p in _d[1:-1].split('\n\n'):
    if _p[:_p.find('\n')].find('Bluetooth')==-1:
        _d='bluetooth'+_p
    else:
        _q=_p[:_p.find('(')]
        exec(f'_d=_self.{_q}.__doc__')
    _f=_d[:_d.find("\n")]
    _m,_o=_f.split('(',1)
    _n=_m+'(self,'+_o
    _q=[]
    for _o in _o[:-1].split(','):
        _q.append(_o.split('=',1)[0])
    _q=','.join(_q)
    if _q:
        _q=','+_q
    exec(f'def {_n}:return self._rpc("{_m}"{_q})')
    exec(f'{_m}.__doc__=_d')
del _p,_d,_q,_f,_m,_n,_o

# Edit by 乘着船 at 2023-2024
