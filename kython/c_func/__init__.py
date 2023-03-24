import sys
from ctypes import POINTER, c_ubyte


if sys.version_info >= (3, 10):
    from typing import TypeAlias
    uint8_ptr:TypeAlias = POINTER(c_ubyte)
else:
    from typing import NewType
    uint8_ptr = NewType('uint8_ptr', POINTER(c_ubyte))