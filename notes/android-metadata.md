# Metadata

Tech. dependencies: OS version, other apps? Source: app store, or automatically from packages? Are there tools that support this?

Useful article on inspecting APK files:

<https://pspdfkit.com/blog/2019/inspecting-apk-files/>

Tools for extracting metadata:

- [APK Analyzer](https://developer.android.com/studio/build/apk-analyzer) (part of [Android Studio](https://developer.android.com/studio/index.html))

- [apk-analyzer](https://developer.android.com/studio/command-line/apkanalyzer.html) (as bove, but command-line version)

- [Apktool](https://ibotpeaches.github.io/Apktool/).

- [axmldec](https://github.com/ytsutano/axmldec) - stand-alone decoder for Android Binary XML

- Perhaps [Androguard](https://github.com/androguard/androguard)

Also:

<https://android.stackexchange.com/questions/9312/how-can-i-verify-the-authenticity-of-an-apk-file-i-downloaded>

## Androguard

Decode Android Manifest (printed to screen; strangely redirect to file results in garbage):

```
androguard axml com.Triplee.TripleeSocial.apk
```
