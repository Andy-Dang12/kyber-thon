from ctypes import cdll, cast, create_string_buffer
from ctypes import c_int, c_size_t, c_ubyte, POINTER
import numpy as np
import os

aes256ctr_ref = cdll.LoadLibrary(os.path.abspath(os.path.join(
    __file__,'..','..', 'ref/libpqcrystals_aes256ctr_ref.so')))

def prf():
    pqcrystals_kyber_aes256ctr_ref_prf = aes256ctr_ref.aes256ctr_ref
    pqcrystals_kyber_aes256ctr_ref_prf.argtypes = [POINTER(c_ubyte), c_size_t, POINTER(c_ubyte), POINTER(c_ubyte)]
    pqcrystals_kyber_aes256ctr_ref_prf.restype = None
    
    return


def init():
    return


def squeezeblocks():
    return

