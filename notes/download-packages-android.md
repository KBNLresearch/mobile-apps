# Local download of installers

- Various online services exist, but safety/trustworthiness often not clear. Also some of these sites appear to repackage the original data, so impossible verify authenticity. Not recommended.

- There are also a number of (OS) tools, but many are abondoned projects that no longer work. After experimenting with some of these tools I did have success with [gplaycli](https://github.com/matlink/gplaycli), "a command line tool to search, install, update Android applications from the Google Play Store". 

APK can be downloaded by their App ID, e.g.:

```
gplaycli -d com.Triplee.TripleeSocial
```

This does result in a warning:

```
/home/johan/.local/lib/python3.6/site-packages/gpapi/googleplay.py:645: RuntimeWarning: Unexpected end-group tag: Not all data was converted
  response = googleplay_pb2.ResponseWrapper.FromString(response.content)
```

BUT does result in 81 MB APK file! Issue is [documented here](https://github.com/matlink/gplaycli/issues/272), and there's a pull request with a fix.

## Verify downloaded APK

To verify the authenticity of the APK, I did this:

In a VM, I installed the app from the Google Play store.

Then I used the [Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb) tool on my host machine download the APK from the VM [^1]. Steps:

1. Connect to the VM using its IP address:

  ```
  adb connect 127.0.0.1
  ```

2. Get list of installed packages (redirect output to file):

  ```
  adb shell pm list packages > packages.txt
  ```

3. Lookup package id this file (in this case com.Triplee.TripleeSocial). Then get file path of package: 

  ```
  adb shell pm path com.Triplee.TripleeSocial
  ```

  Result:

  ```
  package:/data/app/com.Triplee.TripleeSocial-r8iVFUp1MOSAc6LmHA1MDQ==/base.apk
  ```

4. Download the package:

  ```
  adb pull /data/app/com.Triplee.TripleeSocial-r8iVFUp1MOSAc6LmHA1MDQ==/base.apk
  ```

  Result: local file "base.apk'.

I then used the [cmp tool](https://linux.die.net/man/1/cmp) to compare this file against the file I downloaded with gplaycli:

```
cmp base.apk com.Triplee.TripleeSocial.apk
```

In this case no output is produced, which confirms both files are identical.

[^1]: Part of [Android Studio](https://developer.android.com/studio)