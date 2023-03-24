from ctypes import cdll, cast, create_string_buffer
from ctypes import c_int, c_size_t, c_ubyte, POINTER
import numpy as np
import os
from kython.c_func.aes256ctr_ref import (
    C_aes256ctr_ctx, 
    pqcrystals_kyber_aes256ctr_ref_prf           as prf,
    pqcrystals_kyber_aes256ctr_ref_init          as init,
    pqcrystals_kyber_aes256ctr_ref_squeezeblocks as squeezeblocks
)

def prf():
    
    return


def init():
    return


def squeezeblocks():
    return

