from ctypes import create_string_buffer
from ctypes import c_uint8, c_char
from typing import List


def strBuffer_to_list(strBuff:'c_char*int'):
    return [int.from_bytes(d, byteorder='little') for d in strBuff]

def list_to_strBuffer(xs:List[c_uint8]) -> 'c_char*int':
    return create_string_buffer(bytes(xs), len(xs))

# from ctypes import create_string_buffer
# x0 = [1, 0, 2]
# xs = create_string_buffer(bytes(x0), len(x0))
# x1 = [int.from_bytes(d, byteorder='little') for d in xs]

# print(x1) # [1, 0, 2, 0]
