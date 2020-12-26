# -*- coding: utf-8 -*-
import subprocess
import sys
import os


valgrind_env = os.environ.copy()
valgrind_env["PYTHONMALLOC"] = "malloc"
valgrind_env["PYTHONPATH"] = "build/tests"
valgrind_cmd = [
    "valgrind",
    "--gen-suppressions=all",
    "--error-exitcode=1",
    "--leak-check=full",
    "--read-var-info=yes",
    "--track-origins=yes",
    "--show-leak-kinds=definite,indirect",
    "--errors-for-leak-kinds=definite,indirect",
]
pytest_cmd = [sys.executable, "-m", "pytest", "tests"]
subprocess.check_call(valgrind_cmd + pytest_cmd, env=valgrind_env)
