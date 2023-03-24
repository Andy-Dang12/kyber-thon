import os.path
from ctypes import (
    cdll, POINTER, Structure, c_size_t, 
    c_size_t, c_uint8, c_uint32, c_uint64
)

"""
* more detail, see 
* ref/aes256ctr.h
* ref/aes256ctr.c
"""
aes256ctr_ref = cdll.LoadLibrary(os.path.abspath(os.path.join(
    __file__,'..', '..','..', 'ref', 'libpqcrystals_aes256ctr_ref.so')))


class C_aes256ctr_ctx(Structure):
    _fields_ = [
        ('sk_exp', c_uint64 * 120),
        ('ivw', c_uint32 * 16)
    ]


#* prf
pqcrystals_kyber_aes256ctr_ref_prf = aes256ctr_ref.pqcrystals_kyber_aes256ctr_ref_prf
pqcrystals_kyber_aes256ctr_ref_prf.argtypes = [POINTER(c_uint8), 
                                               c_size_t, 
                                               POINTER(c_uint8) * 32, 
                                               POINTER(c_uint8) * 12]
pqcrystals_kyber_aes256ctr_ref_prf.restype = None


#* init
pqcrystals_kyber_aes256ctr_ref_init = aes256ctr_ref.pqcrystals_kyber_aes256ctr_ref_init
pqcrystals_kyber_aes256ctr_ref_init.argtypes = [POINTER(C_aes256ctr_ctx), 
                                                POINTER(c_uint8) * 32, 
                                                POINTER(c_uint8) * 12]
pqcrystals_kyber_aes256ctr_ref_init.restype = None


#* squeezeblocks
pqcrystals_kyber_aes256ctr_ref_squeezeblocks = aes256ctr_ref.pqcrystals_kyber_aes256ctr_ref_squeezeblocks
pqcrystals_kyber_aes256ctr_ref_squeezeblocks.argtypes = [POINTER(c_uint8), 
                                                         c_size_t, 
                                                         POINTER(C_aes256ctr_ctx)]
pqcrystals_kyber_aes256ctr_ref_squeezeblocks.restype = None
