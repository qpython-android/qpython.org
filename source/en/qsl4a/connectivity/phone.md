# Phone API

Control phone calls and retrieve phone information.

## Phone State Tracking

### startTrackingPhoneState()
Start tracking phone state changes. Generates 'phone' events.

```python
startTrackingPhoneState()
```

### readPhoneState()
Read the current phone state.

```python
readPhoneState()
```

**Returns:** Bundle with phone state and incoming number

### stopTrackingPhoneState()
Stop tracking phone state.

```python
stopTrackingPhoneState()
```

## Making Calls

### phoneCall()
Call a contact/phone number by URI.

```python
phoneCall(uri)
```

**Parameters:**
- `uri` (str): Contact URI or phone number URI

### phoneCallNumber()
Call a phone number directly.

```python
phoneCallNumber(phone_number)
```

**Parameters:**
- `phone_number` (str): Phone number to call

### phoneDial()
Dial a number (opens dialer without calling).

```python
phoneDial(uri)
```

**Parameters:**
- `uri` (str): Contact URI or phone number URI

### phoneDialNumber()
Dial a phone number (opens dialer without calling).

```python
phoneDialNumber(phone_number)
```

**Parameters:**
- `phone_number` (str): Phone number

## Cell Location

### getCellLocation()
Get the current cell location.

```python
getCellLocation()
```

**Returns:** JSONObject with cell location data

### getAllCellsLocation()
Get all cell locations (for dual SIM devices).

```python
getAllCellsLocation()
```

**Returns:** JSONArray of cell locations

## Network Information

### getNetworkOperator()
Get the MCC+MNC of the current operator.

```python
getNetworkOperator()
```

**Returns:** String (e.g., '310260')

### getNetworkOperatorName()
Get the name of the current operator.

```python
getNetworkOperatorName()
```

**Returns:** String (e.g., 'T-Mobile')

### getNetworkType()
Get the current network type.

```python
getNetworkType()
```

**Returns:** String describing radio technology (e.g., 'LTE', 'UMTS', 'GSM')

### getPhoneType()
Get the phone type.

```python
getPhoneType()
```

**Returns:** String (e.g., 'GSM', 'CDMA', 'SIP')

## SIM Information

### getSimCountryIso()
Get the ISO country code for the SIM.

```python
getSimCountryIso()
```

**Returns:** String (e.g., 'us')

### getSimOperator()
Get the MCC+MNC of the SIM operator.

```python
getSimOperator()
```

**Returns:** String (e.g., '310260')

### getSimOperatorName()
Get the SIM operator name.

```python
getSimOperatorName()
```

**Returns:** String (e.g., 'T-Mobile')

### getSimSerialNumber()
Get the SIM serial number.

```python
getSimSerialNumber()
```

**Returns:** String SIM serial number

### getSimState()
Get the SIM card state.

```python
getSimState()
```

**Returns:** String describing SIM state

### getSubscriberId()
Get the subscriber ID.

```python
getSubscriberId()
```

**Returns:** String subscriber ID

## Voice Mail

### getVoiceMailAlphaTag()
Get the voice mail alpha tag.

```python
getVoiceMailAlphaTag()
```

**Returns:** String voice mail tag

### getVoiceMailNumber()
Get the voice mail number.

```python
getVoiceMailNumber()
```

**Returns:** String voice mail number

## Device Information

### getDeviceId()
Get the device ID (IMEI for GSM). Deprecated.

```python
getDeviceId()
```

**Returns:** String device ID

### getDeviceSoftwareVersion()
Get the device software version.

```python
getDeviceSoftwareVersion()
```

**Returns:** String software version

### getLine1Number()
Get the line 1 phone number.

```python
getLine1Number()
```

**Returns:** String phone number

### checkNetworkRoaming()
Check if connected to roaming network.

```python
checkNetworkRoaming()
```

**Returns:** True if roaming

## Cell Info

### getAllCellInfo()
Get information about all cells.

```python
getAllCellInfo()
```

**Returns:** List of cell information

### setDataEnabled()
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
