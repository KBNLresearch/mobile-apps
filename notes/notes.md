# Mobile apps, raw notes

All info in these raw notes eventually to be moved/edited into more structured docs.

## Avonturen van Max

<https://www.armazing.nl/product/de-avonturen-van-max-op-zoek-naar-fl/>

> De app kan op elke telefoon of tablet gedownload worden. De camera richt je op iedere rechterbladzijde van het boek. Daar wordt een extra laag op getoverd die het verhaal vertelt in de vorm van bewegende 3D-modellen en een vertelster. Zo kan een kind helemaal zelf het verhaal volgen en bekijken. Nog een pluspunt van dit boek, is de update van de app. Het boek blijft de hetzelfde, maar na elke update van de app worden er nieuwe modellen toegevoegd en verbeterd!

"Dit Nederlandse prentenboek heeft wisselende 3D-afbeeldingen" (achtergrondinfo): 

<https://www.iculture.nl/nieuws/nederlands-kinderboek-augmented-reality/>

Website (niet meer online):

<http://www.deavonturenvanmax.nl/>

IA:

<https://web.archive.org/web/20170908190422/http://deavonturenvanmax.nl/>

Bevat appstore/playstore links. Playstore:

<https://play.google.com/store/apps/details?id=com.ARmazing.ARBooks>

But this returns a "We're sorry, the requested URL was not found on this server".

MAAR, site ontwikkelaar zegt (<https://www.armazing.nl/faq/>):

> Het kan zijn dat je zoekt naar ons oude applicatie (ARmazing) we hebben een nieuwe applicatie wat ARize heet.

Link:


<https://play.google.com/store/apps/details?id=com.Triplee.TripleeSocial>

- Version 3.0.6.1
- 25 September 2020
- Requires Andoid 7.0 and up.

Appstore:


<https://apps.apple.com/am/app/triple-e/id1230115561>

Requires iTunes, which is not available for Linux (tried via Wine, but installation fails bc of Windows 10 dependency).

Paper "Considerations on the Acquisition and Preservation of Mobile eBook Apps":

<https://zenodo.org/record/3460450>

Page 3:

> The appearance and functionality of apps in this
> category varied, though a notable shared characteristic
> was that not all content was contained in the app
> package, with each requiring an internet connection or
> a fee to be paid in order to unlock access to additional
> content.

Also, several YouTube videos here:

<https://www.youtube.com/channel/UCPEDDkRVC7jegjC02-7VsUw/videos>

"Hoe werkt mijn boek?"

<https://youtu.be/h4syCHftyCs>

Downloaden + opslaan als documentatie / contextinfo!


# Emulation

## Android

Good overview in [Android emulators entry on Emulation General Wiki](https://emulation.gametechwiki.com/index.php/Android_emulators); LOTS of detail about emulator-specific issues.

- [Anbox](https://anbox.io/) (Android in a Box) - "Run Android applications on any GNU/Linux operating system". Recommended by Emulation General Wiki, so needs checking out!

- Android Emulator (part of [Android Studio](https://developer.android.com/studio/intro)), [Android x86](https://www.android-x86.org/) (e.g. VM in VirtualBox).

- Virtualbox - used to work back in 2015, but latest Android-x86 version ([9, rc 2](https://www.android-x86.org/releases/releasenote-9-0-r2.html)) results in various issues on VirtualBox. These are documented [here](https://forums.virtualbox.org/viewtopic.php?f=4&t=96610). So for the moment not a viable option.

- QEmu - actually the Android-86 [release notes](https://www.android-x86.org/releases/releasenote-9-0-r2.html)  describe how this works.

- [Cuttlefish](]https://source.android.com/setup/create/cuttlefish) - "a configurable virtual Android device that can run both remotely (using third-party cloud offerings such as Google Cloud Engine) and locally (on Linux x86 machines)".



## Location of packages on Android

Default apps:

```
/system/app/
```

Self-installed apps:

```
/data/app/
```

APKs in each folder. BUT trying to `ls' any of these folders gives "Permission denied". Explanation [here](https://stackoverflow.com/questions/1043322/why-do-i-get-access-denied-to-data-folder-when-using-adb).

### Install Arize app from Play store

Works, but keeps crashing on startup. Package under `/data/app/com.Triplee.TripleeSocial-hvwhatever==/base.apk`

## iOS

[iOS Simulator](https://docs.expo.io/workflow/ios-simulator/); but this only works in macOS (no Windows / Linux / VM). From paper Pennock, May & Day:

> The iOS SDK simulator is used for development and
> testing purposes. This could in theory be used to deliver
> content on a PC but would require permission from the
> publisher and extensive user testing. There would also
> be challenges in enabling the simulator independently
> of the full SDK environment. The iOS operating system
> is closed and highly proprietary, limiting the availability
> of alternative emulator sources.

And:

> The proprietary nature of iOS
> remains at this point an unresolved challenge that limits
> the viability of emulation as a preservation approach for
> IPA apps and which will require positive engagement
> with Apple to reach a satisfactory conclusion.

[iOS emulators entry on Emulation General Wiki](https://emulation.gametechwiki.com/index.php/IOS_emulators)

> Unlike their direct competitor, Android-based smartphones, they have currently no usable emulators, as the official iOS SDK (macOS-only) only allows for running your own projects, i.e. they run code generated for an x86 target rather than ARM code as used by iOS. 

Also, see the "History of Failed iOS Emulation Attempts".

[iOS on QEMU](https://github.com/alephsecurity/xnu-qemu-arm64) - interesting, but no support for devices (screen!) at this stage.

## Virtual Box setup

Android-86:

<https://www.android-x86.org/>

Steps:

<https://www.technipages.com/install-android-virtualbox>

<!-->
<https://www.android-x86.org/documentation/virtualbox.html>

-->

Android version: [9.0](https://osdn.net/projects/android-x86/releases/71931)

## Other emulators

Several listed here:

<https://www.techradar.com/best/the-best-android-emulator>


Mostly proprietary products geared towards gaming.

[Prime OS](https://primeos.in/) (website down 28/01/2021).

Also:

[Testing Android apps on a virtual machine](https://www.sjoerdlangkemper.nl/2020/05/06/testing-android-apps-on-a-virtual-machine/) -looks useful; also links to [pre-built VirtualBox images based on Android x86](https://www.osboxes.org/android-x86/).

## Download APK locally

Use [googleplaydownloader](https://framagit.org/tuxicoman/googleplaydownloader) (Linux only)

Installation: [Debian package, in source repo, v 2.4-1](https://framagit.org/tuxicoman/googleplaydownloader/-/blob/master/packages/googleplaydownloader_2.4-1_all.deb)

Has 58 dependencies, so didn't bother trying! BUT source repo includes (modified/updated version of?) Google Play API, which has functionality for downloading:

<https://framagit.org/tuxicoman/googleplaydownloader/-/tree/master/googleplaydownloader/ext_libs/googleplayapi>


This, in turn, is taken from the APK Crawler tool:

<https://github.com/opengapps/apkcrawler>

But code in googleplaydownloader looks more recent (python 3 fixes). API functions (login, search, download) in:

<https://framagit.org/tuxicoman/googleplaydownloader/-/blob/master/googleplaydownloader/ext_libs/googleplayapi/googleplay.py>

BUT results in login error.

Other project based on same code:

<https://github.com/krnick/GooglePlay-API>

README says:

> You need to login on below website before use this package. https://accounts.google.com/b/0/DisplayUnlockCaptcha If show up SecurityCheckError when you modify the code also need to re-login.

So this might be worth a try.

Alternative:

<https://github.com/matlink/gplaycli>

Installed & used:

```
gplaycli -d com.Triplee.TripleeSocial
```

Results in error message:

```
[Errno 2] No such file or directory: '/home/johan/.cache/gplaycli/token'
/home/johan/.local/lib/python3.6/site-packages/gpapi/googleplay.py:645: RuntimeWarning: Unexpected end-group tag: Not all data was converted
  response = googleplay_pb2.ResponseWrapper.FromString(response.content)
```

BUT does result in 81 MB APK file!


Via:

<https://www.lifewire.com/how-to-sideload-android-apps-4689188>


<https://www.apkmirror.com/>

BUT getting login errors with googleplaydownloader code.

TODO test with other (more recent) fork of API:

<https://github.com/NoMore201/googleplay-api>




"APKMirror Free and safe Android APK downloads"

BUT Max app not listed!

Similar site:

<https://apkgk.com/com>

Has Max app (but not latest version):

<https://apkgk.com/com.Triplee.TripleeSocial>

Similar site:

<https://apkcombo.com>

BUT according to [virusTotal scan](https://www.virustotal.com/gui/url/ea7ae3587f1f9d47e4fa2c2fbf99d9e10da99da1ce6918e49f3c87ad41ca0d0d/detection) site may be malicious.

Yet another one:

<https://apkpure.com>

Has latest version of app:

<https://apkpure.com/arize-augmented-reality/com.Triplee.TripleeSocial>

Downloaded as XAPK file, described as "Base APK + Split APKs".

BUT installation requires dedicated APKPure App:

<https://apkpure.com/how-to-install-apk.html>

BUT actually this is just a ZIP file that contains apks + json file.

Evozi APK Downloader:

<https://apps.evozi.com/apk-downloader/>

ZIP file that contains apks + json file; files inside ZIP are identical to those in APKPure ZIP file (same MD5 hashes).

(see also <https://www.wikihow.com/Download-an-APK-File-from-the-Google-Play-Store>)

<https://android.stackexchange.com/questions/12330/how-can-i-download-an-apk-file-from-the-play-store>


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

# Immer app

<https://immer.app/>

## Android app

- v. 1.17
- 9 december 2020
- Needs Android 7 or more recent
