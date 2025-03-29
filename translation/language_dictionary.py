#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Igbo keyword dictionaries

This is the MIT license:
http://www.opensource.org/licenses/mit-license.php

Copyright (c) 2019~ Roland|Chima and contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

# Igbo keywords
class IgboKeyword():
    """
    python igbo keyword
    """
    title = "kiiwords wuru n'ime"
    description = "kiiwords wuru n'ime Python"
    keyword = {
        # logic
        "ma": "and",
        "obu": "or",
        "ezi": "True",
        "asi": "False",
        "odighi": "None",

        # def
        "kowa": "def",
        "udi ihe": "class",
        "onwe": "self",
        "uwa": "global",

        # import
        "site": "from",
        "bubata": "import",
        "dika": "as",

        # flow
        "laghachi": "return",
        "gafere": "pass",
        "bulie": "raise",
        "gaa nihu": "continue",

        # control
        "oburu": "if",
        "oburu na": "elif",
        "ozo": "else",

        # for loop
        "maka": "for",
        "nime": "in",
        "obughi nime": "not in",

        # while loop
        "mgbe": "while",
        "kwusi": "break",

        # try
        "nwa le": "try",
        "wezuga": "except",
        "nikpaazu": "finally",
        "ikwuputa": "assert",

        # build in methods
        "exek": "exec",
        "lamuda": "lambda",
        "deputa": "print",
        "na": "with",
        "meputa": "yield",
    }


class igbo_buildin_method():
    """
    python igbo methods
    """
    title = "odiniime oru"  # internal python functions
    description = "odiniime oru Python"
    keyword = {
        "ntinye": "input",

        # build-in types
        "stl": "str",
        "bool": "bool",
        "ndeputa": "list",
        "dicti": "dict",
        "tupul": "tuple",
        "seti": "set",
        "frozenseti": "frozenset",
        "chl": "chr",
        "ord": "ord",
        "failu": "file",

        # number methods
        "int": "int",
        "float": "float",
        "complexi": "complex",
        "hex": "hex",
        "abs": "abs",
        "cmp": "cmp",

        # string methods
        "malitena": "startswith",
        "mechiena": "endswith",
        "sonye": "join",
        "Kewaa": "split",
        "dochie": "replace",
        "enkoodu": "encoding",
        "dekoodu": "decoding",

        # list methods
        "gbakwunye": "append",
        "gbatia": "extend",
        "tinye": "insert",
        "tufuo": "pop",
        "nkeozo": "next",
        "wepu": "remove",
        "tugharia": "reverse",
        "guo": "count",
        "onodu": "index",
        "hazie": "sort",

        # dict methods
        "igodo": "keys",
        "uru": "values",
        "ihe": "items",
        "melite": "update",
        "dere": "copy",

        # set methods
        "anyado": "clear",
        "gbako": "add",
        "tufuoya": "discard",
        "njiko": "union",
        "nrutu": "intersection",
        "odiiche": "difference",  # ọdịiche
        "symmetric_difference": "symmetric_difference",

        # file methods
        "meghe": "open",
        "guba": "read",  # gụọ comflict
        "dee": "write",
        "guo ahiri": "readline",
        "guoo ahiri": "readlines",
        "mechie": "close",

        # OO
        "callable": "callable",
        "dir": "dir",
        "inweattr": "getattr",
        "iheattr": "hasattr",
        "setiattr": "setattr",
        "onwunwe": "property",

        # build in functions
        "lenz": "len",
        "kacha elu": "max",
        "kacha ala": "min",

        # build in methods
        "kowaa": "enumerate",
        "le ma kowa": "eval",
        "yochaa": "filter",
        "maapu": "map",
        "usoro onu ogugu": "range",
        "xrenji": "xrange",
        "chikota": "sum",
        "udi": "type",
        "ihea": "object",
        "kekota": "zip",
        "nyeaka": "help",
        "obodo": "locals",
        "uwaa": "globals",
        "usoroklass": "classmethod",  ####Unclear_translation
    }


class igbo_exception():
    """
    python igbo exceptions
    Built-in exception keyword
    """
    title = "wezuga"
    description = "wezuga kiiword diniime Python"
    keyword = {
        "Naani": "Exception",
        "Mmejo": "Error",
        # error
        "MmejoAlithmetic": "ArithmeticError",
        "MmejoAssertion": "AssertionError",
        "MmejoAttribute": "AttributeError",
        "NdumoduDeprecation": "DeprecationWarning",
        "MmejoEO": "EOFError",
        "MmejoEnvironment": "EnvironmentError",
        "MmejoFloatingPoint": "FloatingPointError",
        "MmejoIO": "IOError",
        "MmejoIbubata": "ImportError",
        "MmejoIndentation": "IndentationError",
        "MmejoIndex": "IndexError",
        "MmejoKii": "KeyError",
        "KiiboardIntellupt": "KeyboardInterrupt",
        "MmejoLookup": "LookupError",
        "MmejoMemory": "MemoryError",
        "MmejoAha": "NameError",
        "AdighiImplemented": "NotImplemented",
        "MmejoAdighiImplemented": "NotImplementedError",
        "MmejoOS": "OSError",
        "MmejoOverflow": "OverflowError",
        "NdumoduOverflow": "OverflowWarning",
        "MmejoReference": "ReferenceError",
        "MmejoRuntime": "RuntimeError",
        "NdumoduRuntime": "RuntimeWarning",
        "MmejoStandard": "StandardError",
        "KwusiIteration": "StopIteration",
        "MmejoSyntax": "SyntaxError",
        "NdumoduSyntax": "SyntaxWarning",
        "MmejoSystem": "SystemError",
        "SystemEgzit": "SystemExit",
        "MmejoType": "TypeError",
        "MmejoTab": "TabError",
        "MmejoUnboundLocal": "UnboundLocalError",
        "MmejoUnicode": "UnicodeError",
        "NdumoduUser": "UserWarning",
        "MmejoValue": "ValueError",
        "ido aka na nti": "Warning",
        "MmejoWindows": "WindowsError",
        "MmejoZeroDivision": "ZeroDivisionError",
        "MmejoUnicodeDecode": "UnicodeDecodeError",
    }


class igbolang():
    """
    ibolang igbo keyword plugin
    """
    title = "ibpy"
    description = "kiiword diniime iby"
    keyword = {
        "ibpy": "ibpy",
        "Isiusoro": 'if __name__=="__main__"',
        # must do 'from ibpy import ib_exec'/' first
        "ibpyexec": "ib_exec",

        # logic
        "==": "==",
        "!==": "!=",
        "obughi": "not",
        "bu": "is",
        "obughi kwa": "is not",

        # private
        "doc": "doc",
        "init": "init",
        "del": "del",
        "repr": "repr",
        "inwa": "test",
    }


# enter simplified Igbo dict here
class igbo_sys():
    """
    ibpy sys module simplified Igbo plugin
    """
    title = "sistem"
    description = "modulu sistem"
    keyword = {"sys": "sys",
               "mbipute": "version",
               "argv": "argv",
               "egzit": "exit",
               "getfilesystemencoding": "getfilesystemencoding",
               "modulu": "modules",
               "platform": "platform",
               "stderr": "stderr",
               "stdin": "stdin",
               "stdout": "stdout",

               # sys path with list methods
               "uzo": "path",
               }


class igbo_traceback():
    """
    ibpy traceback simplified Igbo plugin
    """
    title = "sistem"
    description = "modulu sistem"
    keyword = {"ikowasi obughi bu": "is not defined",
               "aha": "name",
               "akara": "line",
               "Failu": "File",
               "abaghiuru": "invalid",
               "syntax": "syntax",
               }


#    [ibpy.igbodict]
keyword = IgboKeyword()
method = igbo_buildin_method()
exception = igbo_exception()
ibpy = igbolang()
sys = igbo_sys()
trace = igbo_traceback()

trans = dict(keyword.keyword, **method.keyword)
trans = dict(trans, **exception.keyword)
trans = dict(trans, **ibpy.keyword)
trans = dict(trans, **sys.keyword)
trans = dict(trans, **trace.keyword)
