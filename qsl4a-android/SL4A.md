# QPython SL4A Facade RPC Methods

This document lists all @Rpc annotated methods from the QPython SL4A facade classes.

---

## AndroidFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| setClipboard | text(String) | void | Put text in the clipboard. |
| getClipboard | | String | Read text from the clipboard. |
| startActivityForResult | action(String), uri(optional), type(optional), extras(optional), packagename(optional), classname(optional), flags(optional) | Intent | Starts an activity and returns the result. |
| startActivityForResultIntent | intent(Intent) | Intent | Starts an activity and returns the result. |
| startActivity | action(String), uri(optional), type(optional), extras(optional), wait(optional), packagename(optional), classname(optional), flags(optional) | void | Starts an activity. |
| sendBroadcast | action(String), uri(optional), type(optional), extras(optional), packagename(optional), classname(optional), flags(optional) | void | Send a broadcast. |
| makeIntent | action(String), uri(optional), type(optional), extras(optional), categories(optional), packagename(optional), classname(optional), flags(optional) | Intent | Create an Intent. |
| startActivityIntent | intent(Intent), wait(optional) | void | Start Activity using Intent |
| sendBroadcastIntent | intent(Intent) | void | Send Broadcast Intent |
| vibrate | duration(Integer, default=300) | void | Vibrates the phone or a specified duration in milliseconds. |
| makeToast | message(String), length(Integer, default=0), isHtml(Boolean, default=false), backColor(optional), textColor(optional), textSize(Integer, default=0), textAlign(Integer, default=0) | void | Displays a Toast notification. |
| notify | title(String), message(String), uri(optional), arg(optional) | void | Displays a notification that will be canceled when the user clicks on it. |
| getNetworkStatus | | boolean | Returns the status of network connection. |
| getIntent | | Object | Returns the intent that launched the script. |
| getPackageVersionCode | packageName(String) | int | Returns package version code. |
| getPackageVersion | packageName(String) | String | Returns package version name. |
| log | message(String) | void | Writes message to logcat. |
| environment | | Map<String, Object> | A map of various useful environment details |
| getConstants | classname(String) | Bundle | Get list of constants (static final fields) for a class |

---

## EventFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| eventClearBuffer | | void | Clears all events from the event buffer. |
| eventRegisterForBroadcast | category(String), enqueue(Boolean, default=true) | boolean | Registers a listener for a new broadcast signal |
| eventUnregisterForBroadcast | category(String) | void | Stop listening for a broadcast signal |
| eventGetBrodcastCategories | | Set<String> | Lists all the broadcast signals we are listening for |
| eventPoll | number_of_events(Integer, default=1) | List<Event> | Returns and removes the oldest n events from the event buffer. |
| eventWaitFor | eventName(String), timeout(optional) | Event | Blocks until an event with the supplied name occurs. |
| eventWait | timeout(optional) | Event | Blocks until an event occurs. |
| eventPost | name(String), data(String), enqueue(Boolean, default=false, optional) | void | Post an event to the event queue. |
| rpcPostEvent | name(String), data(String) | void | Post an event to the event queue. (**Deprecated**, use eventPost) |
| receiveEvent | | Event | Returns and removes the oldest event from the event buffer. (**Deprecated**, use eventPoll) |
| waitForEvent | eventName(String), timeout(optional) | Event | Blocks until an event with the supplied name occurs. (**Deprecated**, use eventWaitFor) |
| startEventDispatcher | port(Integer, default=0, optional) | int | Opens up a socket where you can read for events posted |
| stopEventDispatcher | | void | Stops the event server, you can't read in the port anymore |

---

## LocationFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| locationProviders | | List<String> | Returns availables providers on the phone |
| locationProviderEnabled | provider(String) | boolean | Ask if provider is enabled |
| startLocating | minUpdateTime(Integer, default=60000), minUpdateDistance(Integer, default=30), updateGnssStatus(Boolean, default=false) | void | Starts collecting location data. (starts event "location") |
| readLocation | | Map<String, JSONObject> | Returns the current location as indicated by all available providers. |
| readGnssStatus | | JSONArray | read Global Navigation Satellite System status if Android >= 8. |
| stopLocating | | void | Stops collecting location data. (stops event "location") |
| getLastKnownLocation | | Map<String, JSONObject> | Returns the last known location of the device. |
| geocode | latitude(Double), longitude(Double), maxResults(Integer, default=1) | JSONObject[] | Returns a list of addresses for the given latitude and longitude. |

---

## SensorManagerFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| startSensingTimed | sensorNumber(Integer), delayTime(Integer) | void | Starts recording sensor data to be available for polling. (starts event "sensors") |
| startSensingThreshold | sensorNumber(Integer), threshold(Integer), axis(Integer) | void | Records to the Event Queue sensor data exceeding a chosen threshold. (starts event "threshold") |
| readSensors | | Bundle | Returns the most recently recorded sensor data. |
| stopSensing | | void | Stops collecting sensor data. (stops event "sensors") |
| sensorsGetAccuracy | | Integer | Returns the most recently received accuracy value. |
| sensorsGetLight | | Float | Returns the most recently received light value. |
| sensorsGetStepCounter | | Integer | Returns the most recently step counter. |
| sensorsReadAccelerometer | | List<Float> | Returns the most recently received accelerometer values. |
| sensorsReadMagnetometer | | List<Float> | Returns the most recently received magnetic field values. |
| sensorsReadGyroscope | | List<Float> | Returns the most recently received Gyroscope values. |
| sensorsReadOrientation | | List<Double> | Returns the most recently received orientation values. |

---

## PhoneFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| startTrackingPhoneState | | void | Starts tracking phone state. (starts event "phone") |
| readPhoneState | | Bundle | Returns the current phone state and incoming number. |
| stopTrackingPhoneState | | void | Stops tracking phone state. (stops event "phone") |
| phoneCall | uri(String) | void | Calls a contact/phone number by URI. |
| phoneCallNumber | phone number(String) | void | Calls a phone number. |
| phoneDial | uri(String) | void | Dials a contact/phone number by URI. |
| phoneDialNumber | phone number(String) | void | Dials a phone number. |
| getCellLocation | | JSONObject | Returns the current cell location. |
| getAllCellsLocation | | JSONArray | Returns all the cells location. |
| getNetworkOperator | | String | Returns the numeric name (MCC+MNC) of current registered operator. |
| getNetworkOperatorName | | String | Returns the alphabetic name of current registered operator. |
| getNetworkType | | String | Returns a the radio technology (network type) currently in use on the device. |
| getPhoneType | | String | Returns the device phone type. |
| getSimCountryIso | | String | Returns the ISO country code equivalent for the SIM provider's country code. |
| getSimOperator | | String | Returns the MCC+MNC (mobile country code + mobile network code) of the provider of the SIM. |
| getSimOperatorName | | String | Returns the Service Provider Name (SPN). |
| getSimSerialNumber | | String | Returns the serial number of the SIM, if applicable. |
| getSimState | | String | Returns the state of the device SIM card. |
| getSubscriberId | | String | Returns the unique subscriber ID, for example, the IMSI for a GSM phone. |
| getVoiceMailAlphaTag | | String | Retrieves the alphabetic identifier associated with the voice mail number. |
| getVoiceMailNumber | | String | Returns the voice mail number. |
| checkNetworkRoaming | | Boolean | Returns true if the device is considered roaming on the current network. |
| getDeviceId | index(Integer, default=0) | String | Returns the unique device ID (IMEI for GSM, MEID for CDMA). (**Deprecated**) |
| getMeid | index(optional) | String | MEID for CDMA phones, Need Android >= 8.0. |
| getImei | index(optional) | String | IMEI for GSM phones, Need Android >= 8.0. |
| getDeviceSoftwareVersion | | String | Returns the software version number for the device. |
| getLine1Number | | String | Returns the phone number string for line 1. (requires API O) |
| getAllCellInfo | | List<CellInfo> | Returns all the neighboring cell information of the device. |
| setDataEnabled | enable(Boolean) | void | set data enabled |

---

## SmsFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| smsSend | destinationAddress(String), text(String) | void | Sends an SMS. |
| smsGetMessageCount | unreadOnly(Boolean), folder(String, default="inbox") | Integer | Returns the number of messages. |
| smsGetMessageIds | unreadOnly(Boolean), folder(String, default="inbox") | List<Integer> | Returns a List of all message IDs. |
| smsGetMessages | unreadOnly(Boolean), folder(String, default="inbox"), attributes(optional) | List<JSONObject> | Returns a List of all messages. |
| smsGetMessageById | id(Integer), attributes(optional) | JSONObject | Returns message attributes. |
| smsGetAttributes | | List<String> | Returns a List of all possible message attributes. |
| smsDeleteMessage | id(Integer) | Boolean | Deletes a message. |
| smsMarkMessageRead | ids(JSONArray), read(Boolean) | Integer | Marks messages as read. |

---

## CameraFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| cameraCapturePicture | targetPath(optional), cameraId(Integer, default=0), useAutoFocus(Boolean, default=true) | String | Take a picture and save it to the specified path. |
| takePicture | path(optional) | String | Take Picture with system camera. |
| takeVideo | path(optional), quality(Integer, default=1) | String | Take Video with system camera. |
| cameraSetTorchMode | enabled(Boolean) | void | open or close flash light torch of camera. |

---

## MediaRecorderFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| recorderStartMicrophone | path(optional) | String | Records audio from the microphone and saves it to the given location. |
| recorderStop | | void | Stops a previously started recording. |
| recorderPause | | void | Pause a previously started recording. |
| recorderResume | | void | Resume a previously paused recording. |
| recordAudio | | String | Record Audio with system soundrecorder. |
| recorderStartScreenRecord | path(optional), audio(Integer, default=1), targetPixels(optional), frameRate(Integer, default=30), bitRate(optional), rotation(Boolean, default=false), autoStart(Boolean, default=true) | String | Record screen to a file. |
| recorderStart | | void | Start Media Recorder. |
| imageReaderGetScreenShot | path(optional), delayMilliSec(Integer, default=1000) | String | Capture ScreenShot. |
| recorderCaptureVideo | targetPath(optional), duration(Integer, default=10), cameraId(Integer, default=0), quality(Integer, default=8) | String | Records video from the camera and saves it to the given location. |
| recorderSoundVolumeGetDb | | double | Recorder Sound Volumn Get Db. |
| recorderSoundVolumeDetect | interval(Integer, default=100) | boolean | Recorder Sound Volumn Detect. |
| imageCompress | srcPath(String), destPath(String), targetByteSize(Integer, default=0), targetWidth(Integer, default=0), targetHeight(Integer, default=0) | long | image Compress by targetByteSize, targetWidth, targetHeight. |

---

## MediaPlayerFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| mediaPlay | url(String), tag(String, default="default"), play(Boolean, default=true) | boolean | Open a media file |
| mediaPlayPause | tag(String, default="default") | boolean | pause playing media file |
| mediaPlayStart | tag(String, default="default") | boolean | start playing media file |
| mediaPlayClose | tag(String, default="default") | boolean | Close media file |
| mediaIsPlaying | tag(String, default="default") | boolean | Checks if media file is playing. |
| mediaPlayInfo | tag(String, default="default") | Map<String, Object> | Information on current media |
| mediaPlayList | | Set<String> | Lists currently loaded media |
| mediaPlaySetLooping | enabled(Boolean, default=true), tag(String, default="default") | boolean | Set Looping |
| mediaPlaySeek | msec(Integer), tag(String, default="default") | int | Seek To Position |
| musicPlay | url(String) | boolean | Play a music file (**Deprecated**) |

---

## WifiFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| wifiGetScanResults | | JSONArray | Returns the list of access points found during the most recent Wifi scan. |
| wifiLockAcquireFull | | void | Acquires a full Wifi lock. |
| wifiLockAcquireScanOnly | | void | Acquires a scan only Wifi lock. |
| wifiLockRelease | | void | Releases a previously acquired Wifi lock. |
| wifiStartScan | | Boolean | Starts a scan for Wifi access points. |
| checkWifiState | | Boolean | Checks Wifi state. |
| toggleWifiState | enabled(optional) | Boolean | Toggle Wifi on and off. |
| wifiDisconnect | | Boolean | Disconnects from the currently active access point. |
| wifiGetConnectionInfo | ipConvertToString(Boolean, default=true) | JSONObject | Returns information about the currently active access point. |
| wifiReassociate | | Boolean | Reassociates with the currently active access point. |
| wifiReconnect | | Boolean | Reconnects to the currently active access point. |
| wifiGetApState | | String | get wifi ap state. |
| getConnectedInfo | | JSONArray | get connected hot ip |
| getDhcpInfo | ipConvertToString(Boolean, default=true) | Map<String,Object> | get dhcp info |
| getInternetInterfaceAddress | | Map | get Internet Interface Address |

---

## BluetoothFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| bluetoothActiveConnections | | Map<String, String> | Returns active Bluetooth connections. |
| bluetoothWriteBinary | base64(String), connID(String, default="", optional) | void | Send bytes over the currently open Bluetooth connection. |
| bluetoothReadBinary | bufferSize(Integer, default=4096), connID(String, default="", optional) | String | Read up to bufferSize bytes and return a chunked, base64 encoded string. |
| bluetoothConnect | uuid(String, default=DEFAULT_UUID), address(optional) | String | Connect to a device over Bluetooth. |
| bluetoothAccept | uuid(String, default=DEFAULT_UUID), timeout(Integer, default=0) | String | Listens for and accepts a Bluetooth connection. |
| bluetoothMakeDiscoverable | duration(Integer, default=300) | void | Requests that the device be discoverable for Bluetooth connections. |
| bluetoothWrite | ascii(String), connID(String, default="") | void | Sends ASCII characters over the currently open Bluetooth connection. |
| bluetoothReadReady | connID(String, default="", optional) | Boolean | Returns True if the next read is guaranteed not to block. |
| bluetoothRead | bufferSize(Integer, default=4096), connID(String, default="", optional) | String | Read up to bufferSize ASCII characters. |
| bluetoothReadLine | connID(String, default="", optional) | String | Read the next line. |
| bluetoothGetRemoteDeviceName | address(String) | String | Queries a remote device for it's name or null if it can't be resolved |
| bluetoothGetBondedDevices | | JSONObject | bluetooth Get Bonded Devices |
| bluetoothGetBondedDevicesRssi | interval(optional) | JSONObject | bluetooth Get Bonded Devices Rssi |
| bluetoothGetReceivedDevices | | JSONObject | bluetooth Get Received Devices |
| bluetoothGetLocalName | | String | Gets the Bluetooth Visible device name |
| bluetoothSetLocalName | name(String) | boolean | Sets the Bluetooth Visible device name, returns True on success |
| bluetoothGetScanMode | | int | Gets the scan mode for the local dongle. |
| bluetoothGetConnectedDeviceName | connID(String, default="", optional) | String | Returns the name of the connected device. |
| checkBluetoothState | | Boolean | Checks Bluetooth state. |
| toggleBluetoothState | enabled(optional), prompt(Boolean, default=true) | Boolean | Toggle Bluetooth on and off. |
| bluetoothStop | connID(String, default="", optional) | void | Stops Bluetooth connection. |
| bluetoothGetLocalAddress | | String | Returns the hardware address of the local Bluetooth adapter. |
| bluetoothDiscoveryStart | | Boolean | Start the remote device discovery process. |
| bluetoothDiscoveryCancel | | Boolean | Cancel the current device discovery process. |
| bluetoothIsDiscovering | | Boolean | Return true if the local Bluetooth adapter is currently in the device discovery process. |

---

## ContactsFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| pickContact | | Intent | Display a list of contacts to pick from. |
| pickPhone | | String | Display a list of phone numbers to pick from. |
| contactsGetAttributes | | List<String> | Returns a List of all possible attributes for contacts. |
| contactsGetIds | | List<Integer> | Returns a List of all contact IDs. |
| contactsGet | attributes(optional) | List<JSONObject> | Returns a List of all contacts. |
| contactsGetById | id(Integer), attributes(optional) | JSONObject | Returns contacts by ID. |
| contactsGetCount | | Integer | Returns the number of contacts. |
| queryContent | uri(String), attributes(optional), selection(optional), selectionArgs(optional), order(optional) | List<JSONObject> | Content Resolver Query |
| queryAttributes | uri(String) | JSONArray | Content Resolver Query Attributes |

---

## SettingsFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| setScreenTimeout | value(Integer) | Integer | Sets the screen timeout to this number of seconds. |
| getScreenTimeout | | Integer | Returns the current screen timeout in seconds. |
| checkAirplaneMode | | Boolean | Checks the airplane mode setting. |
| checkRingerSilentMode | | Boolean | Checks the ringer silent mode setting. |
| toggleRingerSilentMode | enabled(optional) | Boolean | Toggles ringer silent mode on and off. |
| toggleVibrateMode | enabled(optional), ringer(optional) | Boolean | Toggles vibrate mode on and off. |
| getVibrateMode | ringer(optional) | Boolean | Checks Vibration setting. |
| getMaxRingerVolume | | int | Returns the maximum ringer volume. |
| getRingerVolume | | int | Returns the current ringer volume. |
| setRingerVolume | volume(Integer) | void | Sets the ringer volume. |
| getMaxMediaVolume | | int | Returns the maximum media volume. |
| getMediaVolume | | int | Returns the current media volume. |
| setMediaVolume | volume(Integer) | void | Sets the media volume. |
| getScreenBrightness | | Integer | Returns the screen backlight brightness. |
| setScreenBrightness | value(optional) | Integer | Sets the the screen backlight brightness. |
| checkScreenOn | | Boolean | Checks if the screen is on or off. |
| isExternalStorageManager | | Boolean | return isExternalStorageManager if Android >= 11. |
| getLocale | | String | Get system language and country. (requires API N) |
| getSysInfo | | Map<String,Object> | get system infomation. |
| getAndroidID | | String | get Android ID |
| getScreenInfo | | Map<String,Object> | get screen infomation. |
| elapsedRealtimeNanos | | Long | Nanoseconds after system startup |
| showScreenLock | | Boolean | Show Screen Lock. (requires API M) |
| getTrafficStats | flags(Integer, default=7) | Map<String,Long> | Get transmit/receive traffic statistics since startup. |
| getAppTxBytes | packageName(String) | Map<String,Long> | get qpython Tx bytes |
| getMemoryInfo | | Map<String,Long> | get Memory Information |

---

## SpeechRecognitionFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| recognizeSpeech | prompt(optional), language(optional), languageModel(optional) | String | Recognizes user's speech and returns the most likely result. |

---

## TextToSpeechFacade (@RpcMinSdk(4))

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| ttsSpeak | message(String), pitch(Double, default=1.0), pitchRate(Double, default=1.0) | void | Speaks the provided message via TTS. |
| ttsIsSpeaking | | Boolean | Returns True if speech is currently in progress. |
| ttsStop | | void | Stop speaking TTS. |

---

## ToneGeneratorFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| generateDtmfTones | phoneNumber(String), toneDuration(Integer, default=100) | void | Generate DTMF tones for the given phone number. |

---

## UiConfig

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| htmlPictureSetSize | widthFixed(optional), heightFixed(optional), widthRatio(optional), heightRatio(optional) | void | Set html picture size. widthFixed or heightFixed = 0 means original picture size. |
| htmlPictureGetSize | | Map<String, Object> | Get html picture size. Returns widthFixed, heightFixed, widthRatio, heightRatio. |

---

## UiFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| dialogCreateInput | title(String, default="Value"), message(String, default="Please enter value:"), defaultText(optional), inputType(optional) | void | Create a text input dialog. |
| dialogCreatePassword | title(String, default="Password"), message(String, default="Please enter password:") | void | Create a password input dialog. |
| dialogSetMessageIsHtml | messageIsHtml(Boolean, default=true) | void | Set dialog message is HTML. |
| dialogGetInput | title(String, default="Value"), message(String, default="Please enter value:"), defaultText(optional), messageIsHtml(Boolean, default=false) | String | Queries the user for a text input. |
| dialogGetPassword | title(String, default="Password"), message(String, default="Please enter password:") | String | Queries the user for a password. |
| dialogCreateSpinnerProgress | title(optional), message(optional), maximum progress(Integer, default=100) | void | Create a spinner progress dialog. |
| dialogCreateHorizontalProgress | title(optional), message(optional), maximum progress(Integer, default=100) | void | Create a horizontal progress dialog. |
| dialogCreateAlert | title(optional), message(optional) | void | Create alert dialog. |
| dialogShowAlert | title(String, default="Alert"), message(String, default="The message of the alert ."), positive(String, default="OK"), negative(optional), neutral(optional), messageIsHtml(Boolean, default=false) | Object | Create and show alert dialog. |
| dialogCreateSeekBar | starting value(Integer, default=50), maximum value(Integer, default=100), title(String), message(String) | void | Create seek bar dialog. |
| dialogCreateTimePicker | hour(Integer, default=0), minute(Integer, default=0), is24hour(Boolean, default=false) | void | Create time picker dialog. |
| dialogCreateDatePicker | year(Integer, default=1970), month(Integer, default=1), day(Integer, default=1) | void | Create date picker dialog. |
| dialogDismiss | | void | Dismiss dialog. |
| dialogShow | | void | Show dialog. |
| dialogSetCurrentProgress | current(Integer) | void | Set progress dialog current value. |
| dialogSetMaxProgress | max(Integer) | void | Set progress dialog maximum value. |
| dialogSetProgressMessage | message(String) | void | Set progress dialog message. |
| dialogSetPositiveButtonText | text(String) | void | Set alert dialog positive button text. |
| dialogSetNegativeButtonText | text(String) | void | Set alert dialog button text. |
| dialogSetNeutralButtonText | text(String) | void | Set alert dialog button text. |
| dialogSetItems | items(JSONArray) | void | Set alert dialog list items. |
| dialogShowSimpleChoice | title(String, default="Alert"), message(String, default="The message of the alert ."), items(optional), positive(String, default="OK"), negative(optional), neutral(optional), messageIsHtml(Boolean, default=false) | Object | Create and show simple choice dialog. |
| dialogSetSingleChoiceItems | items(JSONArray), selected(Integer, default=-1) | void | Set dialog single choice items and selected item. |
| dialogShowSingleChoice | title(String, default="Alert"), message(String, default="The message of the alert ."), items(JSONArray), selected(Integer, default=-1), positive(String, default="OK"), negative(optional), neutral(optional), messageIsHtml(Boolean, default=false) | JSONObject | Create and show single choice dialog. |
| dialogSetMultiChoiceItems | items(JSONArray), selected(optional) | void | Set dialog multiple choice items and selection. |
| dialogShowMultiChoice | title(String, default="Alert"), message(String, default="The message of the alert ."), items(JSONArray), selected(optional), positive(String, default="OK"), negative(optional), neutral(optional), messageIsHtml(Boolean, default=false) | Object | Create and show multi choice dialog. |
| dialogGetResponse | | Object | Returns dialog response. |
| dialogGetSelectedItems | | Set<Integer> | Returns list of items user selected. |
| fullShow | layout(String), title(optional), theme(optional) | List<String> | Show Full Screen. |
| fullDismiss | | void | Dismiss Full Screen. |
| fullQuery | | Map<String, Map<String, String>> | Get Fullscreen Properties. |
| fullQueryDetail | id(String) | Map<String, String> | Get fullscreen properties for a specific widget. |
| fullGetProperty | id(String), property(String) | String | Get a fullscreen property for a specific widget. |
| fullGetProperties | ids(JSONArray), property(String) | JSONArray | Get a fullscreen property for many specific widgets. |
| fullSetProperty | id(String), property(String), value(String) | String | Set a fullscreen widget's property. |
| fullSetProperties | ids(JSONArray), property(String), value(String) | String | Set many fullscreen widgets' property. |
| fullSetList | id(String), list(JSONArray), isHtml(Boolean, default=false), listType(Integer, default=0) | String | Attach a text/html/mixed list to a fullscreen widget. |
| fullSetListSelected | id(String), selected(Object) | String | Attach a html list to a fullscreen widget. |
| fullGetListSelected | id(String) | Object | Attach a multi choice list to a fullscreen widget. |
| fullSetList2 | id(String), list(JSONArray), intRes(JSONArray) | String | Attach a 2-line list to a fullscreen widget. |
| fullSetListHtml | id(String), list(JSONArray) | String | Attach a html list to a fullscreen widget. (**Deprecated**) |
| fullSetTitle | title(String) | void | Set the Full Screen Activity Title. |
| fullKeyOverride | keycodes(JSONArray), enable(Boolean, default=true) | JSONArray | Override default key actions. |
| fullGetScreenShot | path(optional) | String | Get the Full Screen Activity ScreenShot to path. |

---

## WakeLockFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| wakeLockAcquireFull | | void | Acquires a full wake lock (CPU on, screen bright, keyboard bright). |
| wakeLockAcquirePartial | | void | Acquires a partial wake lock (CPU on). |
| wakeLockAcquireBright | | void | Acquires a bright wake lock (CPU on, screen bright). |
| wakeLockAcquireDim | | void | Acquires a dim wake lock (CPU on, screen dim). |
| wakeLockRelease | | void | Releases the wake lock. |

---

## BatteryManagerFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| batteryGetCharge | | Integer | Returns the most recently received battery charge counter uAh. |
| readBatteryData | | Bundle | Returns the most recently recorded battery data. (throws "battery" events) |
| batteryStartMonitoring | | void | Starts tracking battery state. (starts event "battery") |
| batteryStopMonitoring | | void | Stops tracking battery state. (stops event "battery") |
| batteryGetStatus | | Integer | Returns the most recently received battery status data |
| batteryGetHealth | | Integer | Returns the most recently received battery health data |
| batteryGetPlugType | | Integer | Returns the most recently received plug type data |
| batteryCheckPresent | | Boolean | Returns the most recently received battery presence data. |
| batteryGetLevel | | Float | Returns the most recently received battery level (percentage). |
| batteryGetVoltage | | Integer | Returns the most recently received battery voltage. |
| batteryGetCurrent | | Integer | Returns the most recently received battery Current mA. |
| batteryGetTemperature | | Integer | Returns the most recently received battery temperature. |
| batteryGetTechnology | | String | Returns the most recently received battery technology data. |

---

## SignalStrengthFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| getTelephoneSignalStrengthLevel | | int | Returns the Telephone Signal Strength Level. (requires API P) |
| getTelephoneSignalStrengthDetail | | String | Returns the Telephone Signal Strength Detail. (requires API P) |
| startTrackingSignalStrengths | | void | Starts tracking signal strengths. GSM/CDMA/EVDO (starts event "signal_strengths") |
| readSignalStrengths | | Bundle | Returns the current signal strengths. GSM/CDMA/EVDO |
| stopTrackingSignalStrengths | | void | Stops tracking signal strength. GSM/CDMA/EVDO (stops event "signal_strengths") |

---

## ApplicationManagerFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| getLaunchablePackages | needClassName(Boolean, default=false) | Map<String, String> | Returns a list of all launchable packages with class name and application name. |
| getApplicationInfo | packageName(optional) | JSONObject | get Application Info |
| launch | classname(optional), packagename(optional), wait(Boolean, default=true) | void | Start activity with the given classname and/or packagename. |
| getRunningPackages | | Set<String> | Returns a list of packages running activities or services. |
| getInstalledPackages | flag(Integer, default=4) | Map<String,String> | get installed packages |
| forceStopPackage | packageName(String) | void | Force stops a package. |
| checkPermissions | | JSONObject | check all Permissions are granted or denied. |
| requestPermissions | permissions(optional) | void | request Permissions |

---

## CommonIntentsFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| pick | uri(String) | Intent | Display content to be picked by URI (e.g. contacts) |
| scanBarcode | title(optional) | String | Starts the barcode scanner. |
| scanBarcodeFromImage | path(String), sampleSize(Integer, default=0), x(Integer, default=0), y(Integer, default=0), width(Integer, default=0), height(Integer, default=0) | String | scan Barcode From Image |
| view | uri(String), type(optional), extras(optional), wait(Boolean, default=true) | void | Start activity with view action by URI |
| send | uri(String), type(optional), extras(optional), wait(Boolean, default=true) | void | Start activity with send action by URI |
| sendText | text(String), extras(optional), wait(Boolean, default=true) | void | Start activity with send action by text. |
| sendEmail | to(String), subject(String), text(String), path(optional), extras(optional), wait(Boolean, default=true) | void | Launches an activity that sends an e-mail message with a given recipients or attachment. |
| pathToUri | path(String), fileProvider(Boolean, default=true) | String | Convert normal path to content:// . |
| openFile | path(String), type(optional), wait(Boolean, default=true) | void | Open a file with path |
| sendFile | path(Object), type(optional), extras(optional), wait(Boolean, default=true) | void | Send file(s) with path |
| getPathType | path(String) | String | get path type |
| viewMap | query(String), wait(Boolean, default=true) | void | Opens a map search for query |
| viewContacts | wait(optional) | void | Opens the list of contacts. |
| search | query(String) | void | Starts a search for the given query. |
| viewHtml | path(String), title(optional), wait(Boolean, default=true) | void | Opens the browser to display a local HTML/text/audio/video File or http(s) Website. |
| webViewShow | path(String), title(optional), wait(Boolean, default=true) | void | Opens the browser to display a local HTML/text/audio/video File or http(s) Website. (**Deprecated**) |
| videoPlay | path(String), wait(Boolean, default=true) | void | Play the Video via Video Path. |
| editorOpen | path(String) | void | Opens the QEditor to display a local text File. |
| createScriptShortCut | scriptPath(String), label(optional), iconPath(optional), scriptArg(optional) | void | create python script shortcut. |

---

## PreferencesFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| prefGetValue | key(String), filename(optional) | Object | Read a value from shared preferences |
| prefPutValue | key(String), value(Object), filename(optional) | void | Write a value to shared preferences |
| prefGetAll | filename(optional) | Map<String, ?> | Get list of Shared Preference Values |
| prefRemoveValue | key(String), filename(optional) | void | Remove a value from shared preferences |

---

## DocumentFileFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| documentTreeShowOpen | rootPath(String) | Uri | Show Open Document Tree with RootPath. |
| documentFileRenameTo | src(String), dest(String) | boolean | Document File Rename. |
| documentFileDelete | file(String) | boolean | Document File ( or Tree ) Delete. |
| documentFileMkdir | dir(String) | boolean | Document File Make Directorys. |
| documentFileInputStream | srcFile(String), encodingFormat(String, default=""), skip(optional), length(optional) | String | Document File Input Stream. |
| documentFileOutputStream | destFile(String), srcString(String, default=""), encodingFormat(String, default=""), append(optional) | void | Document File Output Stream. |
| documentFileCopy | src(String), dest(String) | void | Document File Copy. |
| documentFileListFiles | folder(String) | JSONArray | Document File List Files. |
| documentFileShowOpen | rootPath(String) | Uri | Show Open Document Tree with RootPath. (**Deprecated**) |
| documentFileMoveTo | src(String), dest(String) | boolean | Document File Move To. (**Deprecated**) |
| documentFileMkdirs | dir(String) | boolean | Document File Make Directorys. (**Deprecated**) |
| documentFileReadFrom | srcFile(String), encodingFormat(String, default=""), skip(optional), length(optional) | String | Document File Read From. (**Deprecated**) |
| documentFileWriteTo | destFile(String), srcString(String, default=""), encodingFormat(String, default=""), append(optional) | void | Document File Write To. (**Deprecated**) |
| documentFileGetUri | path(String), isDirectory(optional) | Uri | Document File Get Uri. |
| documentFileIsDirectory | path(String) | Boolean | Document File Is Directory. |
| documentFileIsFile | path(String) | Boolean | Document File Is File. |
| documentFileExists | path(String) | Boolean | Document File Exists. |
| documentFileLength | path(String) | Long | Document File Length. |
| documentFileLastModified | path(String) | Long | Document File Last Modified. |
| documentFileGetStat | path(String) | Map<String,Object> | Document File Get Stat. |
| getFileStat | path(String) | Map<String,Object> | get file stat. |
| getSdCardPaths | | String[] | get Sd Card Paths. |

---

## FloatViewFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| floatView | args(optional) | int | Show Float View. |
| floatViewResult | index(Integer, default=-1) | JSONObject | Return Float View Result. |
| floatViewRemove | index(Integer, default=-1) | int | Remove Float View. |
| floatViewCount | | int | Float View Count. |
| backgroundProtect | enabled(Boolean, default=true) | void | QPython Background Protect. |

---

## AccessibilityFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| accessibilityStartService | | boolean | Opens system settings to enable accessibility service. |
| accessibilityClick | x(Double, default=0), y(Double, default=0), t(Integer, default=50) | Boolean | Performs a click on the screen at the specified coordinates. |
| accessibilitySlide | XnYn(optional), t(optional) | Boolean | Performs a slide on the screen at the specified coordinates. |
| accessibilityAction | actionCode(Integer, default=0) | Boolean | Performs a accessibility action with the designated action code. |
| accessibilityServiceEnabled | | boolean | Check if accessibility service is enabled. |

---

## ActivityResultFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| setResultBoolean | resultCode(Integer), resultValue(Boolean) | void | Sets the result of a script execution. |
| setResultByte | resultCode(Integer), resultValue(Integer) | void | Sets the result of a script execution. |
| setResultShort | resultCode(Integer), resultValue(Integer) | void | Sets the result of a script execution. |
| setResultChar | resultCode(Integer), resultValue(String) | void | Sets the result of a script execution. |
| setResultInteger | resultCode(Integer), resultValue(Integer) | void | Sets the result of a script execution. |
| setResultLong | resultCode(Integer), resultValue(Long) | void | Sets the result of a script execution. |
| setResultFloat | resultCode(Integer), resultValue(Double) | void | Sets the result of a script execution. |
| setResultDouble | resultCode(Integer), resultValue(Double) | void | Sets the result of a script execution. |
| setResultString | resultCode(Integer), resultValue(String) | void | Sets the result of a script execution. |
| setResultBooleanArray | resultCode(Integer), resultValue(Boolean[]) | void | Sets the result of a script execution. |
| setResultByteArray | resultCode(Integer), resultValue(Integer[]) | void | Sets the result of a script execution. |
| setResultShortArray | resultCode(Integer), resultValue(Integer[]) | void | Sets the result of a script execution. |
| setResultCharArray | resultCode(Integer), resultValue(String[]) | void | Sets the result of a script execution. |
| setResultIntegerArray | resultCode(Integer), resultValue(Integer[]) | void | Sets the result of a script execution. |
| setResultLongArray | resultCode(Integer), resultValue(Long[]) | void | Sets the result of a script execution. |
| setResultFloatArray | resultCode(Integer), resultValue(Double[]) | void | Sets the result of a script execution. |
| setResultDoubleArray | resultCode(Integer), resultValue(Double[]) | void | Sets the result of a script execution. |
| setResultStringArray | resultCode(Integer), resultValue(String[]) | void | Sets the result of a script execution. |
| setResultSerializable | resultCode(Integer), resultValue(Serializable) | void | Sets the result of a script execution. |

---

## CipherFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| cipherInit | key(String), algorithm(String, default="AES/CBC/PKCS5Padding"), encodingFormat(String, default=""), initialVector(Object, default="") | void | Initialize Encrypt Engine / Decrypt Engine. |
| encryptString | srcString(String) | String | Encrypt a Normal / Base64 String to another Base64 String. |
| decryptString | srcString(String) | String | Decrypt a Base64 String to another Normal / Base64 String. |
| encryptStringToFile | srcString(String), dstFile(String) | void | Encrypt a Normal / Base64 String to another File. |
| decryptFileToString | srcFile(String) | String | Decrypt a File to another Normal / Base64 String. |
| encryptFile | srcFile(String), dstFile(String) | void | Encrypt a File to another File. |
| decryptFile | srcFile(String), dstFile(String) | void | Decrypt a File to another File. |

---

## FtpFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| ftpStart | | String[] | FTP Start Service. |
| ftpStop | | void | FTP Stop Service. |
| ftpIsRunning | | boolean | FTP Server is Running. |
| ftpGet | | String[] | FTP Server get IP address. |
| ftpSet | port(optional), rootDir(optional), username(optional), password(optional) | JSONObject | FTP Server set port,rootDir,username,password. |
| ftpStatus | | String | FTP Server get status. |

---

## HarmonyOsFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| getSystemProperty | property(String), defaultValue(String, default="") | String | get System Property |
| getHarmonyOsInformation | | Map<String,String> | get Harmony OS Information. |

---

## QPyInterfaceFacade

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| executeQPyAsSrv | path(optional) | Boolean | Execute QPython script throught SL4A |
| executeQPy | path(String, default=""), arg(optional) | Boolean | Execute QPython script throught SL4A |
| executeQPyCodeAsSrv | code(optional) | Boolean | Execute QPython script throught SL4A |
| executeQPyCode | code(optional) | Boolean | Execute QPython script throught SL4A |
| getLastLog | logName(String, default="last.log") | String | Get last QPython execute log |
| sharedVariableSet | key(String), value(String) | String | set Java Shared Variable. |
| sharedVariableGet | key(String) | String | get Java Shared Variable. |
| sharedVariableRemove | key(String) | String | remove Java Shared Variable. |

---

## WebCamFacade (@RpcMinSdk(8))

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| webcamStart | resolutionLevel(Integer, default=0), jpegQuality(Integer, default=20), port(Integer, default=0) | Object | Starts an MJPEG stream and returns a Tuple of address and port for the stream. |
| webcamAdjustQuality | resolutionLevel(Integer, default=0), jpegQuality(Integer, default=20) | void | Adjusts the quality of the webcam stream while it is running. |
| webcamStop | | void | Stops the webcam stream. |
| cameraStartPreview | resolutionLevel(Integer, default=0), jpegQuality(Integer, default=20), filepath(optional) | boolean | Start Preview Mode. Throws 'preview' events. |
| cameraStopPreview | | void | Stop the preview mode. |

---

## USBHostSerialFacade (@RpcMinSdk(12))

| RPC Method | Parameters | Return | Description |
|------------|------------|--------|-------------|
| usbserialGetDeviceList | | Map<String, String> | Returns USB devices reported by USB Host API. |
| usbserialDisconnect | connID(String, default="", optional) | void | Disconnect all USB-device. |
| usbserialActiveConnections | | Map<String, String> | Returns active USB-device connections. |
| usbserialWriteBinary | base64(String), connID(String, default="", optional) | void | Send bytes over the currently open USB Serial connection. |
| usbserialReadBinary | bufferSize(Integer, default=4096), connID(String, default="", optional) | String | Read up to bufferSize bytes and return a chunked, base64 encoded string. |
| usbserialConnect | hash(String, default=DEFAULT_HASHCODE), options(String, default="") | String | Connect to a device with USB-Host. |
| usbserialHostEnable | | Boolean | Requests that the host be enable for USB Serial connections. |
| getUsbDeviceType | hash(String, default=DEFAULT_HASHCODE) | String | Requests that the type of the device. |
| usbserialWrite | ascii(String), connID(String, default="") | void | Sends ASCII characters over the currently open USB Serial connection. |
| usbserialReadReady | connID(String, default="", optional) | Boolean | Returns True if the next read is guaranteed not to block. |
| usbserialRead | connID(String, default=""), bufferSize(Integer, default=4096, optional) | String | Read up to bufferSize ASCII characters. |
| usbserialGetDeviceName | connID(String, default="", optional) | String | Queries a remote device for it's name or null if it can't be resolved |

---

## Summary

| Facade Class | Number of RPC Methods |
|--------------|----------------------|
| AndroidFacade | 19 |
| EventFacade | 13 |
| LocationFacade | 8 |
| SensorManagerFacade | 11 |
| PhoneFacade | 29 |
| SmsFacade | 8 |
| CameraFacade | 4 |
| MediaRecorderFacade | 12 |
| MediaPlayerFacade | 10 |
| WifiFacade | 15 |
| BluetoothFacade | 25 |
| ContactsFacade | 9 |
| SettingsFacade | 26 |
| SpeechRecognitionFacade | 1 |
| TextToSpeechFacade | 3 |
| ToneGeneratorFacade | 1 |
| WakeLockFacade | 5 |
| BatteryManagerFacade | 13 |
| SignalStrengthFacade | 5 |
| ApplicationManagerFacade | 8 |
| CommonIntentsFacade | 19 |
| PreferencesFacade | 4 |
| DocumentFileFacade | 22 |
| FloatViewFacade | 5 |
| AccessibilityFacade | 5 |
| ActivityResultFacade | 19 |
| CipherFacade | 7 |
| FtpFacade | 6 |
| HarmonyOsFacade | 2 |
| QPyInterfaceFacade | 8 |
| WebCamFacade | 5 |
| USBHostSerialFacade | 12 |

**Total: 32 Facade Classes with 344 RPC Methods**