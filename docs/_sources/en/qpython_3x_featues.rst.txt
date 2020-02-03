QPython 3x featues
==================

QPython 3x, Previously it was QPython3.

A: Why are there so many branches?

Q: Because Google Play and some appstores have strict requirements for application permissions,
they require different permissions, we use different branch codes, for example, 3 means it was QPython3, 
L means LIMITED, S means SENSITIVE permission is required.

A: I know there was a QPython before, what is the difference between it and QPython 3x?

Q: It is now called QPython Ox now, which is mainly aimed at programming learners, and 
it provides more friendly features for beginners. QPython 3x is mainly for experienced 
Python users, and it provides some advanced technical features.


A: Where can I get old versions?

Q: Take a look at `this link <https://github.com/qpython-android/qpython3/releases>`_.

WHAT'S NEW
-----------

QPython 3x v3.0.0 (Published on 2020/2/1)
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

This is the first version after we restarting the QPython project

- It added the `qsl4ahelper <https://github.com/qpython-android/qpython.org/blob/master/qpython-docs/source/en/qpypi.rst>`_ as a built-in package
- It added a `QPySL4A App project sample <https://gist.github.com/riverfor/427c4c8762d5c57468e24ec026bbb0e9>`_ into built-in editor, you can create QSLAApp by creating an project
- It rearranged permissions
- It fixed `ssl error <https://github.com/qpython-android/qpython3/issues/61>`_ bugs

App's Features
-----------------

- Offline Python 3 interpreter: no Internet is required to run Python programs
- It supports running multiple types of projects, including: console program, SL4A program, webapp program
- Convenient QR code reader for transferring codes to your phone
- QPYPI and a custom repository for prebuilt wheel packages for enhanced scientific libraries, such as numpy, scipy, matplotlib, scikit-learn etc
- Easy-to-use editor
- INTEGRATED & EXTENDED SCRIPT LAYER FOR ANDROID LIBRARY (SL4A): IT LETS YOU DRIVE THE ANDROID WORK WITH PYTHON
- Good documentation and customer support


Android Permissions that QPython requires
------------------------------------------

QPython require the BLUETOOTH / LOCATION / BLUETOOTH and OTHER permissions, so that you can program using these FEATURES. AND WE WILL NOT USE THIS PERMISSIONS IN BACKGROUND.

Both QPython 3S and 3L
>>>>>>>>>>>>>>>>>>>>>>

- android.permission.INTERNET
- android.permission.WAKE_LOCK
- android.permission.ACCESS_NETWORK_STATE
- android.permission.CHANGE_NETWORK_STATE
- android.permission.ACCESS_WIFI_STATE
- android.permission.CHANGE_WIFI_STATE
- android.permission.RECEIVE_BOOT_COMPLETED
- android.permission.CAMERA
- android.permission.FLASHLIGHT
- android.permission.VIBRATE
- android.permission.RECEIVE_USER_PRESENT
- com.android.vending.BILLING
- com.android.launcher.permission.INSTALL_SHORTCUT
- com.android.launcher.permission.UNINSTALL_SHORTCUT
- android.permission.READ_EXTERNAL_STORAGE
- android.permission.WRITE_EXTERNAL_STORAGE
- android.permission.READ_MEDIA_STORAGE
- android.permission.ACCESS_COARSE_LOCATION
- android.permission.ACCESS_FINE_LOCATION
- android.permission.FOREGROUND_SERVICE
- android.permission.BLUETOOTH
- android.permission.BLUETOOTH_ADMIN
- android.permission.NFC
- android.permission.RECORD_AUDIO
- android.permission.ACCESS_NOTIFICATION_POLICY
- android.permission.KILL_BACKGROUND_PROCESSES
- net.dinglisch.android.tasker.PERMISSION_RUN_TASKS

QPython 3S
>>>>>>>>>>>
- android.permission.ACCESS_SUPERUSER
- android.permission.READ_SMS
- android.permission.SEND_SMS
- android.permission.RECEIVE_SMS
- android.permission.WRITE_SMS
- android.permission.READ_PHONE_STATE
- android.permission.CALL_PHONE
- android.permission.READ_CALL_LOG
- android.permission.PROCESS_OUTGOING_CALLS
- android.permission.READ_CONTACTS
- android.permission.GET_ACCOUNTS
- android.permission.SYSTEM_ALERT_WINDOW

