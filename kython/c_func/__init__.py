import sys
from ctypes import POINTER, c_ubyte
from .kyber512_ref import (pqcrystals_kyber512_ref_keypair,
                           pqcrystals_kyber512_ref_enc,
                           pqcrystals_kyber512_ref_dec)

if sys.version_info >= (3, 10):
    from typing import TypeAlias
    uint8_ptr:TypeAlias = POINTER(c_ubyte)
else:
    from typing import NewType
    uint8_ptr = NewType('uint8_ptr', POINTER(c_ubyte))