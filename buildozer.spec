[app]

title = TITAN Pro
package.name = titanpro
package.domain = org.titan
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,html,js,css,woff,ttf,md,gif,webp
version = 75.0

# Start lighter: flask core first. numpy/pandas are heavy and often break CI.
# After a successful base APK we can add them back.
requirements = python3,flask,requests,urllib3,jinja2,werkzeug,markupsafe,itsdangerous,click,blinker,certifi,charset-normalizer,idna,six,setuptools

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE,FOREGROUND_SERVICE
android.api = 33
android.minapi = 26
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True
android.presplash_color = #050816

# CRITICAL: webview bootstrap for Flask apps
# (without this, buildozer defaults to sdl2 which is wrong)
p4a.branch = master

# Force webview via requirements token used by some p4a versions
# Also set explicitly if supported:
# android.bootstrap = webview

[buildozer]
log_level = 2
warn_on_root = 0
