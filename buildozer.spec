[app]

title = TITAN Pro
package.name = titanpro
package.domain = org.titan
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,html,js,css,woff,ttf,md,gif,webp
version = 75.0

# FULL requirements - complete TITAN Pro
requirements = python3,flask,numpy,pandas,requests,urllib3,websocket-client,jinja2,werkzeug,markupsafe,itsdangerous,click,blinker,certifi,charset-normalizer,idna,six,pytz,python-dateutil,tzdata,pillow,setuptools

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,ACCESS_NETWORK_STATE,FOREGROUND_SERVICE,MANAGE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 26
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.allow_backup = True
android.presplash_color = #050816

# CRITICAL for Flask: use WebView bootstrap
android.bootstrap = webview
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 0
