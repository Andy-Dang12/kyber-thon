from ctypes import cdll, cast, create_string_buffer
from ctypes import c_int, c_ubyte, POINTER
import numpy as np

# load the shared library containing the C function
libkyber = cdll.LoadLibrary('ref/libpqcrystals_kyber512_ref.so')

def kyber512_ref_keypair() -> tuple[list, list]:
    # define the input and output types for the function
    pqcrystals_kyber512_ref_keypair = libkyber.pqcrystals_kyber512_ref_keypair
    pqcrystals_kyber512_ref_keypair.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte)]
    pqcrystals_kyber512_ref_keypair.restype = c_int

    # allocate memory for the input and output buffers
    pk = create_string_buffer(800)
    sk = create_string_buffer(1632)

    # pass pointers to unsigned bytes to the function
    pk_ptr = cast(pk, POINTER(c_ubyte))
    sk_ptr = cast(sk, POINTER(c_ubyte))
    pqcrystals_kyber512_ref_keypair(pk_ptr, sk_ptr)

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
    return pk_list, sk_list

