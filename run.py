#!/usr/bin/env python3
# Created by Patrick Fu on 2021/3/27.

import os
import sys
import subprocess

"""
This is a demo script and only do one thing that check whether `commitlint` have been installed.

You can copy `check_deps.py` to your repo, and execute it in your build script or 'Pre Build Run Script' in IDE
"""

PROJ_ROOT = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':

    # Check commitlint
    try:
        subprocess.check_call([sys.executable, os.path.join(PROJ_ROOT, 'check_deps.py'), 'commitlint'])
    except Exception:
        print('\nERROR: Missing node module `commitlint`, please `cd` to the root directory of this repo and execute `npm install`\n\n')
        sys.exit(1)
