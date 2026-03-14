# QPython Branches

QPython is the Python engine for Android. It contains amazing features such as Python interpreter, runtime environment, editor, QPYI and integrated SL4A. It makes it easy for you to use Python on Android. And it's FREE.

QPython already has millions of users worldwide and it is also an open source project.

For different usage scenarios, QPython has several branches:

## QPython - IDE for Python & AI

The main version available on Google Play and other app stores. This version focuses on AI features, making it easier for users to learn and use Python in the AI era.

**Key Features:**
- AI-powered coding assistance and learning tools
- Offline Python 3.12 interpreter: no Internet is required to run Python programs
- Supports multiple project types: console, SL4A, webapp
- Convenient QR code reader for transferring codes to your phone
- QPYPI and custom repository for prebuilt wheel packages
- Easy-to-use editor with syntax highlighting
- Good documentation and community support

**Permissions:** Requires only basic phone permissions for installation.

**Download:** Available on Google Play and major app stores.

## QPython+ - Python for Android

The community open-source version (in planning and preparation). This version is designed for contributors who want to participate in QPython project development and supports customization for different manufacturers.

**Key Features:**
- Community-driven development
- Support for vendor customization
- More flexible configuration options
- Open for contributors to join development

**Permissions:** Requires only basic phone permissions for installation.

**Download:** Will be available on Google Play and major app stores.

**Note:** This version is currently in planning and preparation phase. Stay tuned for updates!

## QPython Plus

A special version with extended permissions that provides maximum control over the device. This version is **NOT** published on app stores due to its sensitive permission requirements.

**Key Features:**
- Full SL4A API access including sensitive features
- SMS/Call control APIs
- Advanced system integration
- Maximum device control capabilities

**Permissions:** Requires extensive permissions including:
- Bluetooth
- Location (GPS)
- Read/Send SMS
- Call phone
- Camera and microphone
- System settings
- And other sensitive permissions

**Download:** Not available on app stores. Distributed through special channels only.

**Important:** QPython will not use these permissions in background without your knowledge. If you get exceptions while using SL4A APIs, please check whether the relevant permissions are enabled in system settings.

---

# Amazing Features (All Versions)

- Offline Python 3.12 interpreter: no Internet is required to run Python programs
- It supports running multiple types of projects, including: console program, SL4A program, webapp program
- Convenient QR code reader for transferring codes to your phone
- QPYPI and a custom repository for prebuilt wheel packages for enhanced scientific libraries, such as numpy, scipy, matplotlib, scikit-learn etc
- Easy-to-use editor
- INTEGRATED & EXTENDED SCRIPT LAYER FOR ANDROID LIBRARY (SL4A): IT LETS YOU DRIVE THE ANDROID WORK WITH PYTHON
- Good documentation and customer support

# SL4A Features

With SL4A features, you can use Python programming to control Android work:

- Android Apps API, such as: Application, Activity, Intent & startActivity, SendBroadcast, PackageVersion, System, Toast, Notify, Settings, Preferences, GUI
- Android Resources Manager, such as: Contact, Location, Phone, Sms, ToneGenerator, WakeLock, WifiLock, Clipboard, NetworkStatus, MediaPlayer
- Third App Integrations, such as: Barcode, Browser, SpeechRecognition, SendEmail, TextToSpeech
- Hardware Manager: Camera, Sensor, Ringer & Media Volume, Screen Brightness, Battery, Bluetooth, SignalStrength, WebCam, Vibrate, NFC, USB

[API Documentation Link]
https://github.com/qpython-android/qpysl4a/blob/master/README.md

[API Samples]
https://github.com/qpython-android/qpysl4a/issues/1

# How To Get Professional Customer Support

Please follow the guide to get support https://github.com/qpython-android/qpython/blob/master/README.md

[QPython community]
https://www.facebook.com/groups/qpython

# FAQ

**Q: Why can't I use the SMS API of SL4A?**

A: Different QPython versions have different permission levels:

- **QPython - IDE for Python & AI**: Basic permissions, some sensitive APIs may not be available
- **QPython+**: Basic permissions, community version for development
- **QPython Plus**: Full permissions including SMS, Call, and other sensitive features

If you cannot use certain SL4A APIs, check which version you have installed and consider switching to the appropriate version for your needs.