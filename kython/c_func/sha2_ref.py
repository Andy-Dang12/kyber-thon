from os.path import abspath, join
from ctypes import cdll, POINTER, c_size_t, c_size_t, c_uint8

"""
* more detail, see 
* ref/sha2.h
* ref/sha256.c
* ref/sha512.c
"""

sha2_ref = cdll.LoadLibrary(abspath(join(
    __file__,'..', '..', '..', 'ref', 'libpqcrystals_sha2_ref.so')))


#* sha256
pqcrystals_sha2_ref_sha256 = sha2_ref.pqcrystals_sha2_ref_sha256
pqcrystals_sha2_ref_sha256.restype  = None
pqcrystals_sha2_ref_sha256.argtypes = [POINTER(c_uint8) * 32,
                                       POINTER(c_uint8),
                                       c_size_t]

#* sha512
pqcrystals_sha2_ref_sha512 = sha2_ref.pqcrystals_sha2_ref_sha512
pqcrystals_sha2_ref_sha512.restype  = None
pqcrystals_sha2_ref_sha512.argtypes = [POINTER(c_uint8) * 64,
                                       POINTER(c_uint8),
                                       c_size_t]
