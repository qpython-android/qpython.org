# Phone API

Control phone calls and retrieve phone information.

## Phone State Tracking

### startTrackingPhoneState() *ASL4A*
Start tracking phone state changes. Generates 'phone' events.

```python
startTrackingPhoneState()
```

### readPhoneState() *ASL4A*
Read the current phone state.

```python
readPhoneState()
```

**Returns:** Bundle with phone state and incoming number

### stopTrackingPhoneState() *ASL4A*
Stop tracking phone state.

```python
stopTrackingPhoneState()
```

## Making Calls

### phoneCall() *ASL4A*
Call a contact/phone number by URI.

```python
phoneCall(uri)
```

**Parameters:**
- `uri` (str): Contact URI or phone number URI

### phoneCallNumber() *ASL4A*
Call a phone number directly.

```python
phoneCallNumber(phone_number)
```

**Parameters:**
- `phone_number` (str): Phone number to call

### phoneDial() *ASL4A*
Dial a number (opens dialer without calling).

```python
phoneDial(uri)
```

**Parameters:**
- `uri` (str): Contact URI or phone number URI

### phoneDialNumber() *ASL4A*
Dial a phone number (opens dialer without calling).

```python
phoneDialNumber(phone_number)
```

**Parameters:**
- `phone_number` (str): Phone number

## Cell Location

### getCellLocation() *ASL4A*
Get the current cell location.

```python
getCellLocation()
```

**Returns:** JSONObject with cell location data

### getAllCellsLocation() *ASL4A*
Get all cell locations (for dual SIM devices).

```python
getAllCellsLocation()
```

**Returns:** JSONArray of cell locations

## Network Information

### getNetworkOperator() *ASL4A*
Get the MCC+MNC of the current operator.

```python
getNetworkOperator()
```

**Returns:** String (e.g., '310260')

### getNetworkOperatorName() *ASL4A*
Get the name of the current operator.

```python
getNetworkOperatorName()
```

**Returns:** String (e.g., 'T-Mobile')

### getNetworkType() *ASL4A*
Get the current network type.

```python
getNetworkType()
```

**Returns:** String describing radio technology (e.g., 'LTE', 'UMTS', 'GSM')

### getPhoneType() *ASL4A*
Get the phone type.

```python
getPhoneType()
```

**Returns:** String (e.g., 'GSM', 'CDMA', 'SIP')

## SIM Information

### getSimCountryIso() *ASL4A*
Get the ISO country code for the SIM.

```python
getSimCountryIso()
```

**Returns:** String (e.g., 'us')

### getSimOperator() *ASL4A*
Get the MCC+MNC of the SIM operator.

```python
getSimOperator()
```

**Returns:** String (e.g., '310260')

### getSimOperatorName() *ASL4A*
Get the SIM operator name.

```python
getSimOperatorName()
```

**Returns:** String (e.g., 'T-Mobile')

### getSimSerialNumber() *ASL4A*
Get the SIM serial number.

```python
getSimSerialNumber()
```

**Returns:** String SIM serial number

### getSimState() *ASL4A*
Get the SIM card state.

```python
getSimState()
```

**Returns:** String describing SIM state

### getSubscriberId() *ASL4A*
Get the subscriber ID.

```python
getSubscriberId()
```

**Returns:** String subscriber ID

## Voice Mail

### getVoiceMailAlphaTag() *ASL4A*
Get the voice mail alpha tag.

```python
getVoiceMailAlphaTag()
```

**Returns:** String voice mail tag

### getVoiceMailNumber() *ASL4A*
Get the voice mail number.

```python
getVoiceMailNumber()
```

**Returns:** String voice mail number

## Device Information

### getDeviceId() *ASL4A*
Get the device ID (IMEI for GSM). Deprecated.

```python
getDeviceId()
```

**Returns:** String device ID

### getDeviceSoftwareVersion() *ASL4A*
Get the device software version.

```python
getDeviceSoftwareVersion()
```

**Returns:** String software version

### getLine1Number() *ASL4A*
Get the line 1 phone number.

```python
getLine1Number()
```

**Returns:** String phone number

### checkNetworkRoaming() *ASL4A*
Check if connected to roaming network.

```python
checkNetworkRoaming()
```

**Returns:** True if roaming

## Cell Info

### getAllCellInfo() *ASL4A*
Get information about all cells.

```python
getAllCellInfo()
```

**Returns:** List of cell information

### setDataEnabled() *ASL4A*
Enable or disable mobile data.

```python
setDataEnabled(enabled)
```

**Parameters:**
- `enabled` (bool): True to enable, False to disable

## Usage Example

```python
import androidhelper

droid = androidhelper.Android()

# Get network info
operator = droid.getNetworkOperatorName().result
print(f"Operator: {operator}")

network_type = droid.getNetworkType().result
print(f"Network: {network_type}")

# Get SIM info
sim_state = droid.getSimState().result
print(f"SIM: {sim_state}")

# Get phone number
line1 = droid.getLine1Number().result
print(f"Phone: {line1}")

# Track phone state
droid.startTrackingPhoneState()
print("Tracking phone state...")
droid.stopTrackingPhoneState()
```
