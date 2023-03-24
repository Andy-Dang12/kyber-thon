from ctypes import cdll, c_int, c_uint8, POINTER
from os.path import abspath, join


"""
* more detail, see 
* ref/kem.h
* ref/kem.c
"""

kyber512_ref = cdll.LoadLibrary(abspath(join(
    __file__,'..','..','..', 'ref', 'libpqcrystals_kyber512_ref.so')))


#* keypair
pqcrystals_kyber512_ref_keypair = kyber512_ref.pqcrystals_kyber512_ref_keypair
pqcrystals_kyber512_ref_keypair.argtypes = [POINTER(c_uint8), POINTER(c_uint8)]
pqcrystals_kyber512_ref_keypair.restype = c_int


#* enc
pqcrystals_kyber512_ref_enc = kyber512_ref.pqcrystals_kyber512_ref_enc
pqcrystals_kyber512_ref_enc.argtypes = [POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)]
pqcrystals_kyber512_ref_enc.restype = c_int


#* dec
pqcrystals_kyber512_ref_dec = kyber512_ref.pqcrystals_kyber512_ref_dec
pqcrystals_kyber512_ref_dec.argtypes = [POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)]
pqcrystals_kyber512_ref_dec.restype = c_int

