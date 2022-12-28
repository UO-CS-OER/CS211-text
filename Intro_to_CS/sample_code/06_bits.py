"""Sample code for chapter 6,
manipulating binary numbers
"""
from typing import Tuple


def pack_4_4(x: int, y: int) -> int:
    """Pack two 4-bit values into an
    8-bit value.
    x and y must be in range 0..15 inclusive.
    Result is in range 0..255 inclusive.
    """
    assert 0 <= x <= 15
    assert 0 <= y <= 15
    return (x << 4) | y


def unpack_4_4(packed: int) -> Tuple[int, int]:
    """Unpack an 8 bit value into two 4-bit values,
    treating bits 0..3 and 4..7 as non-negative
    integers, returned as a tuple.
    """
    # Extract bits 0..3
    y = (0b1111) & packed
    # Extract bits 4..7
    x = ((0b11110000) & packed) >> 4
    return (x, y)


assert unpack_4_4(pack_4_4(5, 9)) == (5, 9)
assert unpack_4_4(pack_4_4(15, 0)) == (15, 0)
assert unpack_4_4(pack_4_4(0, 15)) == (0, 15)
assert unpack_4_4(pack_4_4(15, 15)) == (15, 15)
assert unpack_4_4(pack_4_4(0, 0)) == (0, 0)


def rgb_pack(r: int, g: int, b: int) -> int:
    """Pack the red, green, and blue values into an integer"""
    rgb = (r << 16) | (g << 8) | b
    return rgb


def rgb_unpack(rgb: int) -> Tuple[int, int, int]:
    """Unpack rgb color into r, g, b components"""
    b = rgb & 255
    rg = rgb >> 8
    g = rg & 255
    r = rg >> 8
    return (r, g, b)


purple = rgb_pack(255, 0, 255)
assert purple == 0xff00ff
r, g, b = rgb_unpack(purple)
assert r == 255 and g == 0 and b == 255
