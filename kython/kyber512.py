from ctypes import cdll, cast, create_string_buffer
from ctypes import c_int, c_ubyte, POINTER
import numpy as np

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
    pqcrystals_kyber512_ref_keypair.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte)]
    pqcrystals_kyber512_ref_keypair.restype = c_int

    # allocate memory for the input and output buffers
    pk = create_string_buffer(800)
    sk = create_string_buffer(1632)

    # pass pointers to unsigned bytes to the function
    pk_ptr = cast(pk, POINTER(c_ubyte))
    sk_ptr = cast(sk, POINTER(c_ubyte))
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


def kyber512_ref_enc(pk_ptr:POINTER(c_ubyte)):
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
    pqcrystals_kyber512_ref_enc.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), POINTER(c_ubyte)]
    pqcrystals_kyber512_ref_enc.restype = c_int
    
    ct = create_string_buffer(768)
    ss = create_string_buffer(32)
    
    # pass pointers to unsigned bytes to the function
    ct_ptr = cast(ct, POINTER(c_ubyte))
    ss_ptr = cast(ss, POINTER(c_ubyte))
    res = pqcrystals_kyber512_ref_enc(ct_ptr, ss_ptr, pk_ptr)
    
    ct_list = [int.from_bytes(ct[i:i+1], byteorder='little') for i in range(len(ct))]
    ss_list = [int.from_bytes(ss[i:i+1], byteorder='little') for i in range(len(ss))]
    
    ct_array = np.frombuffer(ct, dtype="uint8")
    ss_array = np.frombuffer(ss, dtype="uint8")
    return ct_list, ss_list, ct, ss, ct_ptr, ss_ptr


def kyber512_ref_dec():
    return 


def test_keys():
    pk_list, sk_list, pk, sk, pk_ptr, sk_ptr = kyber512_ref_keypair()
    ct_list, ss_list, ct, ss, ct_ptr, ss_ptr = kyber512_ref_enc(pk_ptr)

test_keys()
