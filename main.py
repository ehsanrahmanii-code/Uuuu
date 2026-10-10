#!/usr/bin/env python3
"""
TITAN Pro - Android entry point (WebView bootstrap)
Starts the Flask server so the Android WebView can connect to it.
"""
from __future__ import annotations

import os
import sys
import time

# Ensure the project directory is in the path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

def main():
    # Small delay to let Android environment settle
    time.sleep(1.2)

    # Import the main TITAN module
    # The original large file must be named TITAN_PRO_V75_PWA.py in the same folder
    try:
        import TITAN_PRO_V75_PWA as titan
    except ImportError as e:
        print("ERROR: Could not import TITAN_PRO_V75_PWA.py")
        print("Make sure the original file is uploaded to the repository root.")
        print(str(e))
        sys.exit(1)

    # Force host and port for Android WebView bootstrap
    # debug=False is required on Android
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
