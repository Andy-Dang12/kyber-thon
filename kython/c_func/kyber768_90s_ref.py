from ctypes import cdll, c_int, c_uint8, POINTER
from os.path import abspath, join


"""
* more detail, see 
* ref/kem.h
* ref/kem.c
"""

kyber512_ref = cdll.LoadLibrary(abspath(join(
    __file__,'..','..','..', 'ref', 'libpqcrystals_kyber512-90s_ref.so')))