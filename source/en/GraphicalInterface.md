# Graphical Interface (Turtle & Tkinter)

This guide explains how to enable graphical interface support (Turtle and Tkinter) in QPython on Android devices.

![QPython Graphical Interface](static/qpython_graphical_interace_demo.jpg)

## Overview

QPython can run Turtle and Tkinter applications, but requires additional software to provide graphical display support on Android.

## Prerequisites

Before starting, you need to download the following resources:

1. **Xserver.apk** - A companion app that provides graphical support for Turtle/Tkinter
   - Download from: [QPythonProject/Extra on Google Drive](https://www.qpython.org/en/#download-resources)
2. **Turtle & Tkinter QPython graphical interface extension** - Install via QPython's QPYPI

## Installation Steps

### Step 1: Install Xserver

Download and install Xserver.apk from the QPython Extra resources directory on Google Drive.

### Step 2: Install QPython Extension

Open QPython and navigate to QPYPI. Find and install the **Turtle & Tkinter QPython graphical interface** extension.

### Step 3: Configure Xserver Battery Settings

To prevent Xserver from being killed when running in the background:

1. Go to your device's **Settings** > **Apps** > **Xserver**
2. Find **Battery** settings
3. Set battery management to **"Unrestricted"** or **"No restrictions"**

This ensures Xserver continues running when switched to background.

### Step 4: Configure QPython Battery Settings (Recommended)

Similarly, set QPython's battery management to **"Unrestricted"** to prevent process termination:

1. Go to **Settings** > **Apps** > **QPython**
2. Find **Battery** settings
3. Set battery management to **"Unrestricted"**

### Step 5: Launch Xserver

Start the Xserver app and switch it to run as a background task before running your Turtle/Tkinter application.

## Running Turtle/Tkinter Applications

After completing the setup:

1. Ensure Xserver is running in the background
2. Run your Turtle or Tkinter application in QPython
3. Switch to Xserver to view the graphical output

## Demo Program

You can download and try the **Turtle Draw Doraemon** demo program from QPYPI's first extension section of QPython App to verify your setup.

## Troubleshooting

- **Black screen**: Ensure Xserver is running before starting your application
- **Application crashes**: Check that both QPython and Xserver have unrestricted battery settings
- **No display**: Verify the Turtle/Tkinter extension is properly installed via QPYPI
