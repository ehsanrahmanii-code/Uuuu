#!/usr/bin/env python3
"""
TITAN Pro - Android entry point (WebView bootstrap)
Starts the Flask server so the Android WebView can connect to it.
"""
from __future__ import annotations

import os
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

def main():
    time.sleep(1.2)

    # Install numpy/pandas stubs if native packages are missing (Android APK)
    try:
        import titan_compat  # noqa: F401
    except Exception as e:
        print("compat load warning:", e)

    try:
        import TITAN_PRO_V75_PWA as titan
    except ImportError as e:
        print("ERROR: Could not import TITAN_PRO_V75_PWA.py")
        print(str(e))
        sys.exit(1)

    print("Starting TITAN Pro server on 0.0.0.0:5000 ...")
    titan.app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False,
        threaded=True,
    )

if __name__ == "__main__":
    main()
