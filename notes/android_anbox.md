# Test with Anbox

[Anbox](https://github.com/anbox/anbox) "is a container-based approach to boot a full Android system on a regular GNU/Linux system like Ubuntu. In other words: Anbox will let you run Android on your Linux system without the slowness of virtualization".

Some tests (TODO edit below from here):

Chrome browser - ??

Connect with Android Debug Bridge:

```
adb connect 127.0.0.1
```

List devices:

```
adb devices -l
```

Output:

```
```

List packages:

```
adb shell pm list packages
```

Install Arize app:

```
adb install com.Triplee.TripleeSocial.apk
```

Result:

```
```

Launch app: ??
