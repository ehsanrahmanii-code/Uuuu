# TITAN Pro – Android APK

پروژه آماده برای ساخت APK اندروید از روی کد Flask/PWA اصلی TITAN Pro.

## چطور ساخت APK

1. فایل اصلی `TITAN_PRO_V75_PWA.py` را در ریشه اصلی ریپو آپلود کن (یا از مسیر محالی کپی کن).
2. به تب **Actions** برو.
3. ورکفلو **Build TITAN Pro APK** را انتخاب کن.
4. دکمه **Run workflow** را بزن.
5. بعد از اتمام ساخت (ممکن است ۱–۳ ساعت طول بکشد) فایل APK را از بخش **Artifacts** دانلود کن.

## نکات مهم

- اولین بار ساخت بسیار طولانی است چون NDK و recipeهای numpy/pandas باید کامپایل شوند.
- اگر ساخت fail شد، در `buildozer.spec` می‌توانی `android.archs = arm64-v8a` را نگه داری یا requirements را سبک‌تر کنی.
- برای نصب APK روی گوشی باید «نصب از منابع ناشناخته» را فعال کنی.

## ساختار پروژه

- `main.py` → نقطه ورود اندروید (WebView bootstrap)
- `buildozer.spec` → تنظیمات ساخت
- `.github/workflows/build-apk.yml` → ساخت اتوماتیک
- `TITAN_PRO_V75_PWA.py` → فایل اصلی پروژه (باید خودت آپلود کنی)
