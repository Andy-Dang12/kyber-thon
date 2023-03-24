from typing import Tuple, List
from ctypes import c_uint8, POINTER, cast, create_string_buffer
from .c_func import (pqcrystals_kyber512_ref_keypair, 
                     pqcrystals_kyber512_ref_enc, 
                     pqcrystals_kyber512_ref_dec)


def pqc_kyber512_ref_keypair() -> Tuple[List[int], int]:
    pk = b'\x00' * 800
    sk = b'\x00' * 1632
    # pk = create_string_buffer(800)
    # sk = create_string_buffer(1632)
    res = pqcrystals_kyber512_ref_keypair(
        cast(pk, POINTER(c_uint8)),
        cast(sk, POINTER(c_uint8))
    )

    pk = [int.from_bytes(pk[i:i+1], byteorder='little') for i in range(len(pk))]
    sk = [int.from_bytes(sk[i:i+1], byteorder='little') for i in range(len(sk))]
    # pk = [int.from_bytes(d, byteorder='little') for d in pk]
    # sk = [int.from_bytes(d, byteorder='little') for d in sk]
    return pk, sk


def pqc_kyber_ref_enc():
    return
    
def pqc_kyber_ref_dec():
    return
