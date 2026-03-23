# QSL4A (QPython Scripting Layer for Android) - Codebase Analysis

## 1. Package Structure

The QSL4A codebase is located at `/qsl4a/src/main/java/org/qpython/qsl4a/` and is organized into the following packages:

| Package | Purpose |
|---------|---------|
| `org.qpython.qsl4a` (root) | Main entry points (QSL4APP, QPyScriptService, QSL4AScript) |
| `org.qpython.qsl4a.codec` | Base64 encoding/decoding for data serialization |
| `org.qpython.qsl4a.facade` | Android API facades (30+ classes) |
| `org.qpython.qsl4a.facade.ui` | UI-related facade components |
| `org.qpython.qsl4a.facade.usb` | USB serial communication facades |
| `org.qpython.qsl4a.qsl4a` | Core infrastructure |
| `org.qpython.qsl4a.qsl4a.event` | Event system |
| `org.qpython.qsl4a.qsl4a.exception` | Exception types |
| `org.qpython.qsl4a.qsl4a.future` | Async activity handling |
| `org.qpython.qsl4a.qsl4a.interpreter` | Interpreter management |
| `org.qpython.qsl4a.qsl4a.jsonrpc` | JSON-RPC mechanism |
| `org.qpython.qsl4a.qsl4a.language` | Language support |
| `org.qpython.qsl4a.qsl4a.rpc` | RPC annotations and descriptors |
| `org.qpython.qsl4a.qsl4a.trigger` | Event trigger system |
| `org.qpython.qsl4a.qsl4a.util` | Utility classes |

---

## 2. Core Classes

### 2.1 Main Entry Points

#### QSL4APP (`org.qpython.qsl4a.QSL4APP`)
**Purpose:** Application class that initializes the QSL4A runtime environment.

**Key Methods:**
- `initQSL4APP()` - Initializes interpreter configuration and starts discovering interpreters
- `getTaskExecutor()` -> `FutureActivityTaskExecutor` - Returns the task executor
- `getInterpreterConfiguration()` -> `InterpreterConfiguration` - Returns interpreter config
- `getTriggerRepository()` -> `TriggerRepository` - Returns the trigger repository
- `readyToStart()` -> `boolean` - Blocks until configuration is updated

#### QPyScriptService (`org.qpython.qsl4a.QPyScriptService`)
**Purpose:** Android Service that hosts the JSON-RPC server for script execution.

**Key Methods:**
- `onCreate()` - Starts the service and initializes the proxy
- `onDestroy()` - Shuts down the proxy and RPC server
- `onBind(Intent intent)` -> `IBinder` - Returns binder for service connection
- `onStartCommand(Intent intent, int flags, int startId)` -> `int` - Returns START_STICKY
- `start(Context context)` - Static method to start the service
- `stop(Context context)` - Static method to stop the service
- `startToast(Context context)` - Shows toast when service starts

#### QSL4AScript (`org.qpython.qsl4a.QSL4AScript`)
**Purpose:** Utility class for script file handling.

**Key Methods:**
- `getFileName(Context context)` -> `String` - Returns the main script filename (default: "main.py")
- `getFileExtension(Context context)` -> `String` - Returns file extension (e.g., ".py")

---

### 2.2 AndroidProxy (`org.qpython.qsl4a.qsl4a.AndroidProxy`)
**Purpose:** Central proxy class that manages the RPC server and facade factories.

**Key Methods:**
- `AndroidProxy(Service service, Intent intent)` - Constructor; creates JSON-RPC server with secret UUID
- `getAddress()` -> `InetSocketAddress` - Returns server address
- `startLocal()` / `startLocal(int port)` - Starts RPC server on localhost
- `shutdown()` - Shuts down the RPC server
- `getSecret()` -> `String` - Returns the authentication secret
- `getRpcReceiverManagerFactory()` -> `RpcReceiverManagerFactory` - Returns the facade factory

---

### 2.3 SimpleServer (`org.qpython.qsl4a.qsl4a.SimpleServer`)
**Purpose:** Abstract base class for TCP socket servers handling concurrent connections.

**Key Methods:**
- `startLocal(int port)` -> `InetSocketAddress` - Starts server on localhost
- `startPublic(int port)` -> `InetSocketAddress` - Starts server on public interface
- `startAllInterfaces(int port)` -> `InetSocketAddress` - Starts server on all interfaces
- `shutdown()` - Stops the server and closes all connections
- `getNumberOfConnections()` -> `int` - Returns active connection count
- `addObserver(SimpleServerObserver)` / `removeObserver(SimpleServerObserver)` - Observer pattern

**Abstract Methods:**
- `handleConnection(Socket socket)` - Subclasses implement to handle client connections

---

## 3. Facade Classes (Android API Access)

All facades extend `RpcReceiver` and are managed by `FacadeManager`. They expose Android functionality via RPC-annotated methods.

### 3.1 FacadeManager (`org.qpython.qsl4a.facade.FacadeManager`)
**Purpose:** Manages all facade instances and handles RPC invocation with SDK version checking.

**Key Methods:**
- `FacadeManager(int sdkLevel, Service service, Intent intent, Collection<Class<? extends RpcReceiver>> classList)` - Constructor
- `getSdkLevel()` -> `int` - Returns Android SDK level
- `getService()` -> `Service` - Returns the Android service
- `getIntent()` -> `Intent` - Returns the launch intent
- `invoke(Class<? extends RpcReceiver> clazz, Method method, Object[] args)` -> `Object` - Invokes RPC with deprecation/minSdk checks
- `getReceiver(Class<T> clazz)` -> `T` - Gets or creates a facade instance

### 3.2 FacadeConfiguration (`org.qpython.qsl4a.facade.FacadeConfiguration`)
**Purpose:** Registry of all available facade classes.

**Registered Facades (30 total):**
- `AndroidFacade` - Core Android operations
- `ApplicationManagerFacade` - App management
- `CameraFacade` - Camera access
- `CommonIntentsFacade` - Common Android intents
- `ContactsFacade` - Contacts access
- `EventFacade` - Event queue management
- `LocationFacade` - GPS/Location
- `PhoneFacade` - Phone operations
- `MediaRecorderFacade` - Audio recording
- `SensorManagerFacade` - Device sensors
- `SettingsFacade` - System settings
- `SmsFacade` - SMS operations
- `SpeechRecognitionFacade` - Voice input
- `ToneGeneratorFacade` - DTMF tones
- `WakeLockFacade` - Power management
- `WifiFacade` - WiFi operations
- `UiFacade` - UI operations
- `BatteryManagerFacade` - Battery info
- `MediaPlayerFacade` - Media playback
- `PreferencesFacade` - Shared preferences
- `QPyInterfaceFacade` - QPython-specific
- `USBHostSerialFacade` - USB serial
- `CipherFacade` - Cryptography
- `TextToSpeechFacade` - TTS
- `BluetoothFacade` - Bluetooth
- `SignalStrengthFacade` - Signal info
- `WebCamFacade` - Camera
- `FloatViewFacade` - Overlay views
- `DocumentFileFacade` - Document access
- `HarmonyOsFacade` - HarmonyOS compatibility
- `FtpFacade` - FTP server
- `AccessibilityFacade` - Accessibility services

### 3.3 AndroidFacade (`org.qpython.qsl4a.facade.AndroidFacade`)
**Purpose:** Main facade providing core Android functionality.

**Key RPC Methods:**
- `setClipboard(String text)` / `getClipboard()` -> `String` - Clipboard operations
- `startActivity(String action, String uri, ...)` - Start activities
- `startActivityForResult(String action, ...)` -> `Intent` - Activity with result
- `sendBroadcast(String action, ...)` - Send broadcasts
- `makeIntent(String action, ...)` -> `Intent` - Create intents
- `makeToast(String message, int length, ...)` - Show toast notifications
- `notify(String title, String message, String uri, ...)` - Show persistent notifications
- `getNetworkStatus()` -> `boolean` - Check network
- `getIntent()` -> `Object` - Get launch intent
- `getPackageVersion(String packageName)` -> `String` - Get package version
- `environment()` -> `Map<String, Object>` - Environment info
- `getConstants(String classname)` -> `Bundle` - Get class constants
- `vibrate(int duration)` - Vibrate device

### 3.4 EventFacade (`org.qpython.qsl4a.facade.EventFacade`)
**Purpose:** Event queue management for async event handling.

**Key RPC Methods:**
- `eventClearBuffer()` - Clears all events from buffer
- `eventPoll(int number_of_events)` -> `List<Event>` - Returns and removes oldest n events
- `eventWaitFor(String eventName, Integer timeout)` -> `Event` - Blocks until event occurs
- `eventWait(Integer timeout)` -> `Event` - Blocks until any event occurs
- `eventPost(String name, String data, Boolean enqueue)` - Post event to queue
- `startEventDispatcher(int port)` -> `int` - Opens socket for event streaming
- `stopEventDispatcher()` - Stops event server
- `eventRegisterForBroadcast(String category, Boolean enqueue)` -> `boolean` - Register broadcast listener
- `eventUnregisterForBroadcast(String category)` - Unregister broadcast listener
- `eventGetBrodcastCategories()` -> `Set<String>` - Get registered categories

### 3.5 SensorManagerFacade (`org.qpython.qsl4a.facade.SensorManagerFacade`)
**Purpose:** Access device sensors (accelerometer, magnetometer, light, gyroscope, etc.).

**Key RPC Methods:**
- `startSensingTimed(int sensorNumber, int delayTime)` - Starts sensor data collection
- `startSensingThreshold(int sensorNumber, int threshold, int axis)` - Threshold-based sensing
- `readSensors()` -> `Bundle` - Returns most recent sensor data
- `stopSensing()` - Stops sensor collection
- `sensorsGetAccuracy()` -> `Integer` - Get sensor accuracy
- `sensorsGetLight()` -> `Float` - Get light level
- `sensorsReadAccelerometer()` -> `List<Float>` - [x, y, z] acceleration
- `sensorsReadMagnetometer()` -> `List<Float>` - [x, y, z] magnetic field
- `sensorsReadGyroscope()` -> `List<Float>` - [x, y, z] angular speed
- `sensorsReadOrientation()` -> `List<Double>` - [azimuth, pitch, roll]
- `sensorsGetStepCounter()` -> `Integer` - Step count

### 3.6 LocationFacade (`org.qpython.qsl4a.facade.LocationFacade`)
**Purpose:** GPS and network location services.

**Key RPC Methods:**
- `startLocating(int minUpdateTime, int minUpdateDistance, boolean updateGnssStatus)` - Start location updates
- `readLocation()` -> `Map<String, JSONObject>` - Get current location by provider
- `readGnssStatus()` -> `JSONArray` - Get GNSS satellite status (Android 8+)
- `stopLocating()` - Stop location updates
- `getLastKnownLocation()` -> `Map<String, JSONObject>` - Get last known location
- `geocode(double latitude, double longitude, int maxResults)` -> `JSONObject[]` - Reverse geocode
- `locationProviders()` -> `List<String>` - Get available providers
- `locationProviderEnabled(String provider)` -> `boolean` - Check if provider enabled

---

## 4. RPC Mechanism

### 4.1 JSON-RPC Server Architecture

```
JsonRpcServer (extends SimpleServer)
    |
    +-- handleConnection(Socket socket)
    |       |
    |       +-- Reads JSON requests line-by-line
    |       +-- First RPC must be _authenticate with secret
    |       +-- Looks up MethodDescriptor by method name
    |       +-- Invokes method and returns JsonRpcResult
    |
    +-- RpcReceiverManagerFactory
            |
            +-- FacadeManagerFactory
                    |
                    +-- Creates FacadeManager instances
                    +-- Each FacadeManager manages multiple RpcReceivers (Facades)
```

### 4.2 JsonRpcServer (`org.qpython.qsl4a.qsl4a.jsonrpc.JsonRpcServer`)
**Purpose:** TCP-based JSON-RPC server that handles client connections.

**Key Methods:**
- `JsonRpcServer(RpcReceiverManagerFactory managerFactory, String handshake)` - Constructor
- `handleConnection(Socket socket)` - Processes JSON-RPC requests
- `shutdown()` - Notifies all receivers and stops server

**Request Format:**
```json
{"id": 1, "method": "methodName", "params": [arg1, arg2]}
```

**Response Format:**
```json
{"id": 1, "result": {...}, "error": null}
```

### 4.3 RpcReceiverManager (`org.qpython.qsl4a.qsl4a.jsonrpc.RpcReceiverManager`)
**Purpose:** Base class managing RPC receivers (facades) and method lookup.

**Key Methods:**
- `RpcReceiverManager(Collection<Class<? extends RpcReceiver>> classList)` - Initializes receivers and collects RPC methods
- `getReceiver(Class<T> clazz)` -> `T` - Gets or lazily creates facade instance
- `getMethodDescriptor(String methodName)` -> `MethodDescriptor` - Looks up RPC method
- `invoke(Class<? extends RpcReceiver> clazz, Method method, Object[] args)` -> `Object` - Invokes method via reflection
- `shutdown()` - Calls shutdown on all receivers

### 4.4 RpcReceiver (`org.qpython.qsl4a.qsl4a.jsonrpc.RpcReceiver`)
**Purpose:** Abstract base class for all facades.

**Methods:**
- `RpcReceiver(RpcReceiverManager manager)` - Constructor; stores manager reference
- `shutdown()` - Abstract; facades implement cleanup

### 4.5 JsonRpcResult (`org.qpython.qsl4a.qsl4a.jsonrpc.JsonRpcResult`)
**Purpose:** Utility class for building JSON-RPC response objects.

**Static Methods:**
- `empty(int id)` -> `JSONObject` - Creates empty result response
- `result(int id, Object data)` -> `JSONObject` - Creates success response
- `error(int id, Throwable t)` -> `JSONObject` - Creates error response

### 4.6 JsonBuilder (`org.qpython.qsl4a.qsl4a.jsonrpc.JsonBuilder`)
**Purpose:** Converts Java objects to JSON for RPC responses.

**Key Methods:**
- `build(Object data)` -> `Object` - Converts Java object to JSON-compatible type
- `buildBundleItem(Object data)` -> `Object` - Handles Bundle, Uri, byte[] special cases
- `buildJsonMap(Map<String, ?> map)` -> `JSONObject` - Converts Map to JSONObject
- `buildJsonList(List<?> list)` -> `JSONArray` - Converts List to JSONArray
- `buildJsonIntent(Intent intent)` -> `JSONObject` - Converts Intent to JSON
- `buildJsonEvent(Event event)` -> `JSONObject` - Converts Event to JSON

**Supported Type Conversions:**
- `null` -> `JSONObject.NULL`
- `Integer, Long, Double` -> primitive values
- `String, Boolean` -> as-is
- `JSONObject, JSONArray` -> as-is
- `List<?>` -> `JSONArray`
- `Set<?>` -> `JSONArray`
- `Map<?, ?>` -> `JSONObject`
- `Intent` -> `{"data", "type", "extras", "categories", "action", "packagename", "classname", "flags"}`
- `Bundle` -> `JSONObject` with special markers (`\0uri\0`, `\0byte\0`)
- `Event` -> `{"name", "data", "time"}`

### 4.7 MethodDescriptor (`org.qpython.qsl4a.qsl4a.rpc.MethodDescriptor`)
**Purpose:** Describes an RPC method, handles parameter conversion, and invokes methods.

**Key Methods:**
- `collectFrom(Class<? extends RpcReceiver> clazz)` -> `Collection<MethodDescriptor>` - Static; collects @Rpc-annotated methods
- `invoke(RpcReceiverManager manager, JSONArray parameters)` -> `Object` - Invokes RPC with parameter conversion
- `convertParameter(JSONArray parameters, int index, Type type)` -> `Object` - Converts JSON param to Java type
- `buildIntent(JSONObject jsonObject)` -> `Intent` - Builds Intent from JSON
- `getName()` -> `String` - Returns RPC name (or @RpcName value)
- `getHelp()` -> `String` - Generates help text from annotations

**Parameter Type Conversions:**
- `Boolean.class` - from JSON boolean or integer (0/1)
- `Long.class` - from JSON long
- `Double.class` - from JSON double
- `Integer.class` - from JSON int
- `Intent.class` - from JSONObject using `buildIntent()`
- Other types - direct cast from JSON

---

## 5. RPC Annotations

### 5.1 @Rpc (`org.qpython.qsl4a.qsl4a.rpc.Rpc`)
**Purpose:** Marks a method as an RPC endpoint.

**Attributes:**
- `description()` -> `String` - Brief description of the function
- `returns()` -> `String` - Description of return value (default: "")

### 5.2 @RpcParameter (`org.qpython.qsl4a.qsl4a.rpc.RpcParameter`)
**Purpose:** Documents RPC parameters.

**Attributes:**
- `name()` -> `String` - Formal parameter name
- `description()` -> `String` - Parameter description (default: "")

### 5.3 @RpcDefault (`org.qpython.qsl4a.qsl4a.rpc.RpcDefault`)
**Purpose:** Specifies default value for optional parameters.

**Attributes:**
- `value()` -> `String` - Default value as string
- `converter()` -> `Class<? extends Converter>` - Type converter (default: Converter.class)

### 5.4 @RpcOptional (`org.qpython.qsl4a.qsl4a.rpc.RpcOptional`)
**Purpose:** Marks parameter as optional with null default.

### 5.5 @RpcName (`org.qpython.qsl4a.qsl4a.rpc.RpcName`)
**Purpose:** Overrides the RPC method name.

**Attributes:**
- `name()` -> `String` - Custom RPC name

### 5.6 @RpcDeprecated (`org.qpython.qsl4a.qsl4a.rpc.RpcDeprecated`)
**Purpose:** Marks RPC as deprecated.

**Attributes:**
- `value()` -> `String` - Replacement method name
- `release()` -> `String` - Release version when deprecated

### 5.7 @RpcMinSdk (`org.qpython.qsl4a.qsl4a.rpc.RpcMinSdk`)
**Purpose:** Specifies minimum Android SDK version required.

**Attributes:**
- `value()` -> `int` - Minimum SDK level

### 5.8 @RpcStartEvent (`org.qpython.qsl4a.qsl4a.rpc.RpcStartEvent`)
**Purpose:** Indicates RPC starts an event stream.

**Attributes:**
- `value()` -> `String` - Event name

### 5.9 @RpcStopEvent (`org.qpython.qsl4a.qsl4a.rpc.RpcStopEvent`)
**Purpose:** Indicates RPC stops an event stream.

**Attributes:**
- `value()` -> `String` - Event name

---

## 6. Interpreter System

### 6.1 Interpreter (`org.qpython.qsl4a.qsl4a.interpreter.Interpreter`)
**Purpose:** Represents a language interpreter with execution parameters.

**Key Methods:**
- `buildFromMaps(Map<String, String> data, Map<String, String> env, Map<String, String> args)` -> `Interpreter` - Static factory
- `getName()` -> `String` - Interpreter name (e.g., "python")
- `getNiceName()` -> `String` - Display name
- `getExtension()` -> `String` - File extension (e.g., ".py")
- `getBinary()` -> `File` - Path to interpreter binary
- `getScriptCommand()` -> `String` - Command template for script execution
- `getInteractiveCommand()` -> `String` - Command for interactive mode
- `hasInteractiveMode()` -> `boolean` - Whether interactive mode supported
- `getArguments()` -> `List<String>` - CLI arguments
- `getEnvironmentVariables()` -> `Map<String, String>` - Environment variables
- `getLanguage()` -> `Language` - Associated language object
- `getRpcText(String content, MethodDescriptor rpc, String[] values)` -> `String` - Generates RPC call code
- `isInstalled()` -> `boolean` - Whether binary exists

### 6.2 InterpreterConfiguration (`org.qpython.qsl4a.qsl4a.interpreter.InterpreterConfiguration`)
**Purpose:** Discovers and manages installed interpreters via Android package intents.

**Key Methods:**
- `startDiscovering()` / `startDiscovering(String mime)` - Starts interpreter discovery
- `isDiscoveryComplete()` -> `boolean` - Whether discovery finished
- `registerObserver(ConfigurationObserver observer)` - Register for config changes
- `getSupportedInterpreters()` -> `List<? extends Interpreter>` - All known interpreters
- `getInstalledInterpreters()` -> `List<Interpreter>` - Only installed ones
- `getInteractiveInterpreters()` -> `List<Interpreter>` - Those with interactive mode
- `getInterpreterByName(String name)` -> `Interpreter` - Find by name
- `getInterpreterForScript(String scriptName)` -> `Interpreter` - Find by file extension

**Discovery Mechanism:**
- Queries package manager for activities handling `InterpreterConstants.MIME + extension`
- Reads interpreter properties from ContentProvider
- Broadcasts `ACTION_INTERPRETER_ADDED` / `ACTION_INTERPRETER_REMOVED`

### 6.3 InterpreterDescriptor (`org.qpython.qsl4a.qsl4a.interpreter.InterpreterDescriptor`)
**Purpose:** Metadata about an interpreter version.

**Attributes:**
- `getVersion()` -> `String` - Version string
- `getName()` -> `String` - Interpreter name
- `isInstalled()` -> `boolean` - Installation status

### 6.4 SupportedLanguages (`org.qpython.qsl4a.qsl4a.language.SupportedLanguages`)
**Purpose:** Registry mapping file extensions to Language classes.

**Supported Languages:**
| Extension | Language Class |
|-----------|---------------|
| `.html` | HtmlLanguage |
| `.bsh` | BeanShellLanguage |
| `.js` | JavaScriptLanguage |
| `.lua` | LuaLanguage |
| `.pl` | PerlLanguage |
| `.py` | PythonLanguage |
| `.rb` | RubyLanguage |
| `.tcl` | TclLanguage |
| `.php` | PhpLanguage |
| `.sl` | SleepLanguage |
| `.nut` | SquirrelLanguage |

### 6.5 Language (`org.qpython.qsl4a.qsl4a.language.Language`)
**Purpose:** Base class for language-specific code generation.

**Key Methods:**
- `getContentTemplate()` -> `String` - Template for new scripts
- `getImportStatement()` -> `String` - Import statement (overridden per language)
- `getRpcReceiverDeclaration(String rpcReceiver)` -> `String` - RPC receiver instantiation
- `getDefaultRpcReceiver()` -> `String` - Default receiver name (default: "droid")
- `getRpcText(String content, MethodDescriptor rpc, String[] values)` -> `String` - Generates method call
- `autoClose(char token)` -> `String` - Returns closing token for auto-complete

### 6.6 PythonLanguage (`org.qpython.qsl4a.qsl4a.language.PythonLanguage`)
**Purpose:** Python-specific code generation.

**Generated Template:**
```python
import android

droid = android.Android()
```

---

## 7. Trigger System

### 7.1 TriggerRepository (`org.qpython.qsl4a.qsl4a.trigger.TriggerRepository`)
**Purpose:** Persistent storage and management of event triggers.

**Key Methods:**
- `put(Trigger trigger)` - Adds trigger and ensures TriggerService running
- `remove(Trigger trigger)` - Removes trigger
- `getAllTriggers()` -> `Multimap<String, Trigger>` - All triggers by event name
- `isEmpty()` -> `boolean` - Whether any triggers exist
- `addObserver(TriggerRepositoryObserver observer)` - Register for changes
- `bootstrapObserver(TriggerRepositoryObserver observer)` - Register and notify of existing triggers
- `removeObserver(TriggerRepositoryObserver observer)` - Unregister

**Persistence:**
- Serializes to Base64-encoded object stream
- Stores in SharedPreferences under key "TRIGGERS"

### 7.2 Trigger (`org.qpython.qsl4a.qsl4a.trigger.Trigger`)
**Purpose:** Interface for event-driven script execution.

**Methods:**
- `handleEvent(Event event, Context context)` - Called when trigger event occurs
- `getEventName()` -> `String` - Event name this trigger listens for

### 7.3 ScriptTrigger (`org.qpython.qsl4a.qsl4a.trigger.ScriptTrigger`)
**Purpose:** Trigger implementation that launches a script file.

**Key Methods:**
- `ScriptTrigger(String eventName, File script)` - Constructor
- `handleEvent(Event event, Context context)` - Starts script via IntentBuilders
- `getEventName()` -> `String` - Returns registered event name
- `getScript()` -> `File` - Returns script file

### 7.4 Event (`org.qpython.qsl4a.qsl4a.event.Event`)
**Purpose:** Immutable event object for the event queue.

**Attributes:**
- `mName` - Event name
- `mData` - Event data (any object)
- `mCreationTime` - Creation timestamp (milliseconds * 1000)

**Key Methods:**
- `Event(String name, Object data)` - Constructor
- `getName()` / `setName(String name)` - Name accessor
- `getData()` / `setData(Object data)` - Data accessor
- `getCreationTime()` -> `double` - Timestamp
- `nameEquals(String name)` -> `boolean` - Name comparison

### 7.5 EventFacade.EventObserver (`org.qpython.qsl4a.facade.EventFacade.EventObserver`)
**Purpose:** Interface for event notification.

**Methods:**
- `onEventReceived(Event event)` - Called when event occurs

### 7.6 EventServer (`org.qpython.qsl4a.facade.EventServer`)
**Purpose:** TCP server that streams events to connected clients.

**Key Methods:**
- `EventServer(int port)` - Constructor; starts server on specified port
- `getAddress()` -> `InetSocketAddress` - Server address
- `onEventReceived(Event event)` - Broadcasts event to all listeners
- `shutdown()` - Notifies listeners and stops server

---

## 8. Async/Future System

### 8.1 FutureResult (`org.qpython.qsl4a.qsl4a.future.FutureResult<T>`)
**Purpose:** Blocking future for async operation results.

**Key Methods:**
- `set(T result)` - Sets result and unblocks waiters
- `get()` -> `T` - Blocks until result available
- `get(long timeout, TimeUnit unit)` -> `T` - Blocks with timeout
- `isDone()` -> `boolean` - Whether result available
- `cancel(boolean mayInterruptIfRunning)` -> `boolean` - Always returns false

### 8.2 FutureActivityTask (`org.qpython.qsl4a.qsl4a.future.FutureActivityTask<T>`)
**Purpose:** Activity lifecycle wrapper for async UI operations.

**Key Methods:**
- `onCreate()` / `onStart()` / `onResume()` / `onPause()` / `onStop()` / `onDestroy()` - Lifecycle callbacks
- `onActivityResult(int requestCode, int resultCode, Intent data)` - Handle activity result
- `setActivity(Activity activity)` / `getActivity()` -> `Activity` - Activity access
- `setTaskDescription(String title)` - Set task description (for recent apps)
- `setResult(T result)` - Set the task result
- `getResult()` -> `T` - Get the result (blocks)
- `finish()` - Finish the activity
- `startActivity(Intent intent)` / `startActivityForResult(Intent intent, int requestCode)` - Start activities

### 8.3 FutureActivityTaskExecutor (`org.qpython.qsl4a.qsl4a.future.FutureActivityTaskExecutor`)
**Purpose:** Executes FutureActivityTask instances on the main thread.

**Key Methods:**
- `execute(FutureActivityTask<T> task)` - Execute task with activity lifecycle

---

## 9. File Structure Summary

```
/qsl4a/src/main/java/org/qpython/qsl4a/
├── QSL4APP.java                     # Application class
├── QPyScriptService.java           # Android Service (RPC server host)
├── QSL4AScript.java                 # Script file utilities
├── codec/                           # Base64 encoding
├── facade/                          # Android API facades (30+ classes)
│   ├── AndroidFacade.java          # Core Android operations
│   ├── EventFacade.java           # Event queue management
│   ├── LocationFacade.java        # GPS/Location
│   ├── SensorManagerFacade.java    # Device sensors
│   ├── UiFacade.java              # UI operations
│   └── ... (25+ more facades)
├── qsl4a/
│   ├── AndroidProxy.java          # Central proxy/RPC server
│   ├── SimpleServer.java          # TCP socket server base
│   ├── Constants.java             # Intent/action constants
│   ├── event/
│   │   └── Event.java            # Event data class
│   ├── exception/
│   │   └── Sl4aException.java    # Base exception
│   ├── future/
│   │   ├── FutureResult.java     # Async result holder
│   │   ├── FutureActivityTask.java # Activity lifecycle wrapper
│   │   └── FutureActivityTaskExecutor.java
│   ├── interpreter/
│   │   ├── Interpreter.java       # Interpreter descriptor
│   │   ├── InterpreterConfiguration.java # Interpreter discovery
│   │   └── Language.java          # Base language class
│   ├── jsonrpc/
│   │   ├── JsonRpcServer.java    # JSON-RPC TCP server
│   │   ├── RpcReceiver.java      # Base facade class
│   │   ├── RpcReceiverManager.java # Manages facades
│   │   ├── RpcReceiverManagerFactory.java
│   │   ├── JsonRpcResult.java    # Response builder
│   │   └── JsonBuilder.java      # JSON serialization
│   ├── language/
│   │   ├── Language.java         # Base language
│   │   ├── PythonLanguage.java   # Python-specific
│   │   └── SupportedLanguages.java # Extension registry
│   ├── rpc/
│   │   ├── Rpc.java             # @Rpc annotation
│   │   ├── RpcParameter.java    # @RpcParameter annotation
│   │   ├── RpcDefault.java      # @RpcDefault annotation
│   │   ├── RpcOptional.java     # @RpcOptional annotation
│   │   ├── RpcName.java         # @RpcName annotation
│   │   ├── RpcDeprecated.java    # @RpcDeprecated annotation
│   │   ├── RpcMinSdk.java       # @RpcMinSdk annotation
│   │   ├── RpcStartEvent.java   # @RpcStartEvent annotation
│   │   ├── RpcStopEvent.java    # @RpcStopEvent annotation
│   │   └── MethodDescriptor.java # RPC method descriptor
│   ├── trigger/
│   │   ├── Trigger.java         # Trigger interface
│   │   ├── ScriptTrigger.java    # Script launch trigger
│   │   └── TriggerRepository.java # Persistent trigger storage
│   └── util/                     # Utilities
```

---

## 10. Key Data Flow

### 10.1 Script Execution Flow
1. Script is launched (via Intent or direct start)
2. `QPyScriptService` starts via `AndroidProxy`
3. `JsonRpcServer` starts on localhost with random port
4. Script connects via TCP socket
5. First RPC must be `_authenticate(secret)`
6. Script calls RPCs like `droid.makeToast("Hello")`
7. `JsonRpcServer` looks up `MethodDescriptor` via `RpcReceiverManager`
8. `MethodDescriptor.invoke()` converts JSON params to Java types
9. Facade method is invoked via reflection
10. Result is converted back to JSON via `JsonBuilder`
11. Response sent back to client

### 10.2 Event Flow
1. Facade calls `eventPost("sensors", data)` or similar
2. `EventFacade.postEvent()` creates `Event` object
3. Event added to `ConcurrentLinkedQueue<Event>` (max 1024)
4. Named event observers are notified
5. Global event observers are notified
6. `EventServer` broadcasts to all connected TCP clients

### 10.3 Trigger Flow
1. `TriggerRepository.put(trigger)` stores trigger
2. Trigger serialized to SharedPreferences
3. When matching event occurs, `Trigger.handleEvent()` is called
4. `ScriptTrigger` starts script via `IntentBuilders.buildStartInBackgroundIntent()`

---

## 11. All Facade Classes Reference

| Facade Class | Purpose |
|--------------|---------|
| `AccessibilityFacade` | Accessibility services |
| `ActivityResultFacade` | Activity result handling |
| `AndroidFacade` | Core Android operations |
| `ApplicationManagerFacade` | Application management |
| `BatteryManagerFacade` | Battery status |
| `BluetoothFacade` | Bluetooth operations |
| `CameraFacade` | Camera access |
| `CipherFacade` | Cryptography/Encryption |
| `CommonIntentsFacade` | Common Android intents |
| `ContactsFacade` | Contacts access |
| `DocumentFileFacade` | Document file access |
| `EventFacade` | Event queue management |
| `EventServer` | TCP event streaming |
| `FloatViewFacade` | Overlay/floating views |
| `FtpFacade` | FTP server |
| `HarmonyOsFacade` | HarmonyOS compatibility |
| `LocationFacade` | GPS/Location |
| `MediaPlayerFacade` | Media playback |
| `MediaRecorderFacade` | Audio/video recording |
| `MjpegServer` | MJPEG streaming |
| `PhoneFacade` | Phone operations |
| `PreferencesFacade` | Shared preferences |
| `QPyInterfaceFacade` | QPython-specific interface |
| `SensorManagerFacade` | Device sensors |
| `SettingsFacade` | System settings |
| `SignalStrengthFacade` | Signal strength |
| `SmsFacade` | SMS operations |
| `SpeechRecognitionFacade` | Speech recognition |
| `TextToSpeechFacade` | Text-to-speech |
| `ToneGeneratorFacade` | DTMF tones |
| `WakeLockFacade` | Power management |
| `WebCamFacade` | Webcam streaming |
| `WifiFacade` | WiFi operations |
