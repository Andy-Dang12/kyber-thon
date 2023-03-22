import posixpath as P
from typing import Union, Tuple
from ctypes import POINTER, byref, cast, c_ubyte, c_byte, c_int
from ctypes import cdll, create_string_buffer

__lib__    = P.abspath(P.join(__file__, '..', '..', 'ref'))
aes256ctr     = cdll.LoadLibrary(P.join(__lib__, 'libpqcrystals_aes256ctr_ref.so'    ))
fips202       = cdll.LoadLibrary(P.join(__lib__, 'libpqcrystals_fips202_ref.so'      ))
sha2          = cdll.LoadLibrary(P.join(__lib__, 'libpqcrystals_sha2_ref.so'         ))
kyber512      = cdll.LoadLibrary(P.join(__lib__, 'libpqcrystals_kyber512_ref.so'     ))
kyber768      = cdll.LoadLibrary(P.join(__lib__, 'libpqcrystals_kyber768_ref.so'     ))
kyber1024     = cdll.LoadLibrary(P.join(__lib__, 'libpqcrystals_kyber1024_ref.so'    ))
kyber512_90s  = cdll.LoadLibrary(P.join(__lib__, 'libpqcrystals_kyber512-90s_ref.so' ))
kyber768_90s  = cdll.LoadLibrary(P.join(__lib__, 'libpqcrystals_kyber768-90s_ref.so' ))
kyber1024_90s = cdll.LoadLibrary(P.join(__lib__, 'libpqcrystals_kyber1024-90s_ref.so'))


# Define the argument and return types for crypto_kem_keypair
# /bin/bash nm libpqcrystals_kyber512_ref.so
kyber512.pqcrystals_kyber512_ref_keypair.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte)]
kyber512.pqcrystals_kyber512_ref_keypair.restype = c_int

def crypto_kem_keypair() -> Tuple:
    """
    * Name:        crypto_kem_keypair
    *
    * Description: Generates public and private key
    *              for CCA-secure Kyber key encapsulation mechanism
    *
    * Arguments:   - uint8_t *pk: pointer to output public key
    *                (an already allocated array of KYBER_PUBLICKEYBYTES bytes)
    *              - uint8_t *sk: pointer to output private key
    *                (an already allocated array of KYBER_SECRETKEYBYTES bytes)
    *
    * Returns 0 (success)
    *
    * CRYPTO_PUBLICKEYBYTES  = 800
    * CRYPTO_SECRETKEYBYTES  = 1632
    * CRYPTO_CIPHERTEXTBYTES = 768
    * CRYPTO_BYTES           = 32
    """
    
    # Allocate memory for the public and private key arrays
    pk = create_string_buffer(800)  #PK_SIZE = 800
    sk = create_string_buffer(1632) #SK_SIZE = 1632
    pk = cast(pk, POINTER(c_ubyte * 800)).contents
    sk = cast(sk, POINTER(c_ubyte * 1632)).contents
    ret = kyber512.pqcrystals_kyber512_ref_keypair(pk, sk)
    
    if not ret:
        return pk, sk
    else:
        return None, None

if __name__ == '__main__':
    pk, sk = crypto_kem_keypair()
    print(type(pk))
    print(type(sk))
    pk = bytes(pk)
    sk = bytes(sk)
    print(pk)
    print()
    print(sk)