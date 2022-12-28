"""Sample code for chapter on Python internals.
Some of this is adapted from
https://www.ics.uci.edu/~brgallar/week9_3.html
"""

import dis
from io import StringIO
from typing import Callable

def objcode(f: Callable) -> str:
    """Text representation of function bytecode"""
    fakefile = StringIO()
    dis.dis(f, file=fakefile)
    txt = [ dis.code_info(f),
            f"*** BYTE CODE for '{f.__name__}' ***",
            "LINE ----- ADDR OPCODE --------------- OPERAND",
            fakefile.getvalue()
            ]
    return "\n".join(txt)


def simple(a: int, b: int) -> int:
    x = 11
    c = a + b * x
    return c

txt = objcode(simple)
print(txt)

