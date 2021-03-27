#!/usr/bin/env python3
# Created by Patrick Fu on 2021/3/27.

import os, sys

"""
Script for checking dependence
"""

PROJ_ROOT = os.path.dirname(os.path.abspath(__file__))


def __check_node_module(module_name: str, root_path: str) -> bool:
    """
    Check whether the [root_path]/node_modules/[module_name] directory exists locally
    """
    node_modules_path = os.path.join(root_path, 'node_modules')
    module_path = os.path.join(node_modules_path, module_name)
    if not os.path.exists(node_modules_path):
        return False
    if not os.path.exists(module_path):
        return False
    return True


def check_commitlint() -> int:
    """
    Check if commitlint is installed (not required if it is Jenkins)

    Return 0: OK; 1: Check failed!
    """
    if os.environ.get('JENKINS_HOME'):
        return 0
    result = __check_node_module('@commitlint', PROJ_ROOT)
    return 0 if result else 1


def main(argv):
    ACTIONS = {
        'commitlint': check_commitlint,
    }

    if len(argv) != 1 or argv[0] not in ACTIONS:
        __usage()
        return 1
    else:
        return ACTIONS[argv[0]]()


def __usage():
    print("""
    Usage:

    1. Check if `commitlint` is installed

        python3 check_deps.py commitlint

    """)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
