# Test with Android Studio Emulator

[Android Studio](https://developer.android.com/studio/) includes [Android Emulator](https://developer.android.com/studio/run/emulator).

Explained [here](https://developer.android.com/studio/run/managing-avds). It's possible to set up  [Android Virtual Device](https://developer.android.com/studio/run/managing-avds) based on user-specified "hardware profile, system image, storage area, skin, and other properties". Both x86 and ARM system images are available. Uses wizard-like interface, very simple to set up.

As a test I set up a device with Android 9 (same as VirtualBox) using x86 image. Some tests:

Chrome browser - works without crashing.

Connect with Android Debug Bridge (note that again IP address listed in Settings/System/About does not work, but localhost does):

```
adb connect 127.0.0.1
```

List devices:

```
adb devices -l
```

Output:

```
List of devices attached
127.0.0.1:5555         device product:sdk_gphone_x86_arm model:AOSP_on_IA_Emulator device:generic_x86_arm transport_id:9
emulator-5554          device product:sdk_gphone_x86_arm model:AOSP_on_IA_Emulator device:generic_x86_arm transport_id:8
```

Note: 2 devices (don't really understand logic behind this?). Anyway, [use `adb` with `-s` switch and device id to send commands to a specific device](https://developer.android.com/studio/command-line/adb#directingcommands):

```
adb -s 127.0.0.1:5555 shell pm list packages
```

Or:

```
adb -s emulator-5554 shell pm list packages
```

TODO: what's the difference between these 2 devices?

Install Arize app:

```
adb -s 127.0.0.1:5555 install com.Triplee.TripleeSocial.apk
```

Result:

```
Performing Streamed Install
Success
```

Launch app: works! But app needs camera, so let's test with webcam. See [How to use webcam in emulator](https://stackoverflow.com/a/30792615): shut down device, open AVD manager, go to Advanced Settings and set Front and Back Camera fields to Webcam0. However app freezes after some time, and VM becomes unresponsive (adb connect also fails). On re-boot it reboots in this error state. Fix: in AVD manager, change Boot option to "Cold boot".

## Using Emulator from command line

Explained [here](https://developer.android.com/studio/run/emulator-commandline).

## Link with QEMU

From above page:

> The Android Emulator uses the Quick Emulator (QEMU) hypervisor. Initial versions of the Android Emulator used QEMU 1 (goldfish), and later versions use QEMU 2 (ranchu).

