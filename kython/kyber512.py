from ctypes import cdll, cast, create_string_buffer
from ctypes import c_int, c_ubyte, c_uint8, POINTER
import numpy as np
from ctypes import c_char
from typing import List


def strBuffer_to_list(strBuff:'c_char*int'):
    return [int.from_bytes(d, byteorder='little') for d in strBuff]

def list_to_strBuffer(xs:List[c_uint8]) -> 'c_char*int':
    return create_string_buffer(bytes(xs), len(xs))

# load the shared library containing the C function
kyber512_ref = cdll.LoadLibrary('ref/libpqcrystals_kyber512_ref.so')

def kyber512_ref_keypair() -> tuple[list, list]:
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
    # define the input and output types for the function
    pqcrystals_kyber512_ref_keypair = kyber512_ref.pqcrystals_kyber512_ref_keypair
    pqcrystals_kyber512_ref_keypair.argtypes = [POINTER(c_uint8), POINTER(c_uint8)]
    pqcrystals_kyber512_ref_keypair.restype = c_int

    # allocate memory for the input and output buffers
    pk = create_string_buffer(800)
    sk = create_string_buffer(1632)

    # pass pointers to unsigned bytes to the function
    pk_ptr = cast(pk, POINTER(c_uint8))
    sk_ptr = cast(sk, POINTER(c_uint8))
    res = pqcrystals_kyber512_ref_keypair(pk_ptr, sk_ptr)

    # pk and sk now contain the public and private keys, respectively
    # convert pk and sk to lists of integers
    pk_list = [int.from_bytes(pk[i:i+1], byteorder='little') for i in range(len(pk))]
    sk_list = [int.from_bytes(sk[i:i+1], byteorder='little') for i in range(len(sk))]

    # print('pk:', pk_list)
    # print('sk:', sk_list)

    # convert pk and sk to numpy arrays with dtype="uint8"
    pk_array = np.frombuffer(pk, dtype="uint8")
    sk_array = np.frombuffer(sk, dtype="uint8")
    
    # free memory used by pk and sk
    # print(f"Python was just handed {hex(ctypes.addressof(c_string_address.contents))}({ctypes.addressof(c_string_address.contents)}):{phrase.value}")
    # print('pk:', pk_array)
    # print('sk:', pk_array)
    return pk_list, sk_list, pk, sk, pk_ptr, sk_ptr


def kyber512_ref_enc(pk_ptr:POINTER(c_uint8)):
    """
    * Name:        crypto_kem_enc
    *
    * Description: Generates cipher text and shared
    *              secret for given public key
    *
    * Arguments:   - uint8_t *ct: pointer to output cipher text
    *                (an already allocated array of KYBER_CIPHERTEXTBYTES bytes)
    *              - uint8_t *ss: pointer to output shared secret
    *                (an already allocated array of KYBER_SSBYTES bytes)
    *              - const uint8_t *pk: pointer to input public key
    *                (an already allocated array of KYBER_PUBLICKEYBYTES bytes)
    *
    * Returns 0 (success)
    *
    * CRYPTO_PUBLICKEYBYTES  = 800
    * CRYPTO_SECRETKEYBYTES  = 1632
    * CRYPTO_CIPHERTEXTBYTES = 768
    * CRYPTO_BYTES           = 32
    """
    pqcrystals_kyber512_ref_enc = kyber512_ref.pqcrystals_kyber512_ref_enc
    pqcrystals_kyber512_ref_enc.argtypes = [POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)]
    pqcrystals_kyber512_ref_enc.restype = c_int
    
    ct = create_string_buffer(768)
    # ss = create_string_buffer(32)   #key_b
    ss = [72, 101, 108, 108, 111] * 6 + [2, 1]
    print('raw_ss1 = ', ss)
    ss = list_to_strBuffer(ss)
    # pass pointers to unsigned bytes to the function
    ct_ptr = cast(ct, POINTER(c_uint8))
    ss_ptr = cast(ss, POINTER(c_uint8))
    res = pqcrystals_kyber512_ref_enc(ct_ptr, ss_ptr, pk_ptr)
    
    ct_list = [int.from_bytes(ct[i:i+1], byteorder='little') for i in range(len(ct))]
    ss_list = [int.from_bytes(ss[i:i+1], byteorder='little') for i in range(len(ss))]
    print('raw_ss2 = ', ss_list)
    ct_array = np.frombuffer(ct, dtype="uint8")
    ss_array = np.frombuffer(ss, dtype="uint8")
    return ct_list, ss_list, ct, ss, ct_ptr, ss_ptr


def kyber512_ref_dec(ct_ptr:POINTER(c_uint8), sk_ptr:POINTER(c_uint8)):
    """
    * Name:        crypto_kem_dec
    *
    * Description: Generates shared secret for given
    *              cipher text and private key
    *
    * Arguments:   - uint8_t *ss: pointer to output shared secret
    *                (an already allocated array of KYBER_SSBYTES bytes)
    *              - const uint8_t *ct: pointer to input cipher text
    *                (an already allocated array of KYBER_CIPHERTEXTBYTES bytes)
    *              - const uint8_t *sk: pointer to input private key
    *                (an already allocated array of KYBER_SECRETKEYBYTES bytes)
    *
    * Returns 0.
    *
    * On failure, ss will contain a pseudo-random value.
    *
    * CRYPTO_PUBLICKEYBYTES  = 800
    * CRYPTO_SECRETKEYBYTES  = 1632
    * CRYPTO_CIPHERTEXTBYTES = 768
    * CRYPTO_BYTES           = 32
    """
    pqcrystals_kyber512_ref_dec = kyber512_ref.pqcrystals_kyber512_ref_dec
    pqcrystals_kyber512_ref_dec.argtypes = [POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)]
    pqcrystals_kyber512_ref_dec.restype = c_int
    
    ss = create_string_buffer(32)   #key_a
    ss_ptr = cast(ss, POINTER(c_uint8))
    res = pqcrystals_kyber512_ref_dec(ss_ptr, ct_ptr, sk_ptr)
    ss_list = [int.from_bytes(ss[i:i+1], byteorder='little') for i in range(len(ss))]
    return ss_list, ss, ss_ptr


def compare_list(first:list, second:list) -> bool:
    if len(first) != len(second):
        print(f"key_a = {len(first)} ; key_b = {len(second)}")
        return False
    
    for a, b in zip(first, second):
        if a != b:
            return False
    return True

def test_keys() -> bool:
    pk_list, sk_list, pk, sk, pk_ptr, sk_ptr = kyber512_ref_keypair()
    ct_list, key_b, ct, ss, ct_ptr, ss_ptr = kyber512_ref_enc(pk_ptr)
    
    key_a, ss, ss_ptr = kyber512_ref_dec(ct_ptr, sk_ptr)
    # print('py_pk = ', pk_list)
    # print('py_sk = ', sk_list)
    # print('py_ss = ', ss.raw)
    print('py_keyA = ', key_a)
    print('py_keyB = ', key_b)
    
    return compare_list(key_a, key_b)


for i in range(1):
    x = test_keys()
    if not x:
        print(x)
print('done')