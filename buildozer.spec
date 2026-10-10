[app]

# (str) Title of your application
title = TITAN Pro

# (str) Package name
package.name = titanpro

# (str) Package domain (needed for android/ios packaging)
package.domain = org.titan

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,html,js,css,woff,ttf,md,gif,webp

# (str) Application versioning (method 1)
version = 75.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,flask,numpy,pandas,requests,urllib3,websocket-client,jinja2,werkzeug,markupsafe,itsdangerous,click,blinker,certifi,charset-normalizer,idna,six,pytz,python-dateutil,tzdata,pillow,setuptools

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE,FOREGROUND_SERVICE,MANAGE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 26

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Accept Android SDK license
android.accept_sdk_license = True

# (list) Android architecture
# Start with only arm64-v8a for faster builds and smaller APK
android.archs = arm64-v8a

# (bool) Copy library instead of making a libpython.so
#android.copy_libs = 1

# (str) Android entry point, default is ok for most of the cases
#android.entrypoint = org.kivy.android.PythonActivity

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#android.arch = armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk or aar).
# android.release_artifact = aab

# (str) Color of the splash screen when the app is loading
android.presplash_color = #050816

# (str) bootstrap for android (webview is required for Flask)
# Some versions use p4a.bootstrap
p4a.branch = master

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
