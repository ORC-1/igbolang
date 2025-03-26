#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import runpy
import code
from core.core import transpile


def commandline():
    """IgboLang, the programming language in Igbo

    usages:
        igbolang                      Enter REPL
        igbolang <file.igbl>          Execute IgboLang script
        igbolang <file.igbl> [args...] Execute IgboLang script with optional arguments
    """
    if len(sys.argv) < 2:
        # Start interactive REPL mode
        sys.ps1 = "igbl>> "
        banner = "IgboLang, the programming language in Igbo (Interactive Interpreter)"
        code.interact(banner=banner, readfunc=transpile)

    else:

        file_path = sys.argv[1]

        script_args = sys.argv[2:]  # Capture optional arguments

        if not os.path.exists(file_path):
            print(f"igbolang: file '{file_path}' does not exist")

            sys.exit(1)

        sys.path[0] = os.path.dirname(os.path.abspath(file_path))

        with open(file_path) as igbolang:

            python = transpile(src=igbolang)

            code_object = compile(python, file_path, "exec")

            # Set sys.argv to simulate script execution with arguments

            sys.argv = [file_path] + script_args

            runpy.run_module(code_object, mod_name="__main__")


if __name__ == "__main__":
    commandline()
