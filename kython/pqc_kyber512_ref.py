from typing import Tuple, List
from ctypes import c_uint8, POINTER, cast, create_string_buffer
from .c_func import (pqcrystals_kyber512_ref_keypair, 
                     pqcrystals_kyber512_ref_enc, 
                     pqcrystals_kyber512_ref_dec)


def pqc_kyber512_ref_keypair() -> Tuple[List[int], List[int]]:
    # pk = b'\x00' * 800
    # sk = b'\x00' * 1632
    pk = create_string_buffer(800)
    sk = create_string_buffer(1632)
    res = pqcrystals_kyber512_ref_keypair(
        cast(pk, POINTER(c_uint8)),
        cast(sk, POINTER(c_uint8))
    )

    pk = [int.from_bytes(pk[i:i+1], byteorder='little') for i in range(len(pk))]
    sk = [int.from_bytes(sk[i:i+1], byteorder='little') for i in range(len(sk))]
    # pk = [int.from_bytes(d, byteorder='little') for d in pk]
    # sk = [int.from_bytes(d, byteorder='little') for d in sk]
    return pk, sk


def pqc_kyber512_ref_enc(ss:List[int], pk:List[int]) -> List[int]:
    ct = create_string_buffer(768)    
    res = pqcrystals_kyber512_ref_enc(
        cast(ct, POINTER(c_uint8)), 
        cast(create_string_buffer(bytes(ss), len(ss)), POINTER(c_uint8)), 
        cast(create_string_buffer(bytes(pk), len(pk)), POINTER(c_uint8))
    )
    return [int.from_bytes(ct[i:i+1], byteorder='little') for i in range(len(ct))]


def pqc_kyber512_ref_dec(ct:List[int], sk:List[int]) -> List[int]:
    ss = create_string_buffer(32)   #key_a
    res = pqcrystals_kyber512_ref_dec(
        cast(ss, POINTER(c_uint8)), 
        cast(create_string_buffer(bytes(ct), len(ct)), POINTER(c_uint8)),
        cast(create_string_buffer(bytes(sk), len(sk)), POINTER(c_uint8))
    )
    return [int.from_bytes(ss[i:i+1], byteorder='little') for i in range(len(ss))]
