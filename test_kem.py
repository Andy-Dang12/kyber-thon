import numpy as np
from ctypes import c_uint8, POINTER, cast, create_string_buffer
from kython.utils import strBuffer_to_list, list_to_strBuffer, strBuffer_to_npuint8, npuint8_to_strBuffer
from kython.pqc_kyber512_ref import (
    pqc_kyber512_ref_keypair as keypair,
    pqc_kyber512_ref_enc     as encode,
    pqc_kyber512_ref_dec     as decode
)
key_b = [72, 101, 108, 108, 111] * 6 + [2, 1]


pk, sk = keypair()
ct = encode(key_b, pk)
key_a = decode(ct, sk)

# print('\n')
# print('py_pk = ', pk)
# print('py_sk = ', sk)

# print('ss1 =   ', ss1)
# print('key_b = ', key_b)
# print('key_a = ', key_a)
# assert key_a == key_b