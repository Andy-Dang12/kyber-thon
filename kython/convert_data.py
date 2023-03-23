from ctypes import *

def convert_to_array_uint8(data:'c_char*int'):
    size = 32
    key_b = create_string_buffer(size)
    assert len(key_b) == size
    [int.from_bytes(key_b[i], byteorder='little') for i in range(size)]



def compare_list(first:list, second:list) -> bool:
    if len(first) != len(second):
        print(f"key_a = {len(first)} ; key_b = {len(second)}")
        return False
    
    for a, b in zip(first, second):
        if a != b:
            return False
    return True


def cvt2_list(x:'c_char*int'):
    return [int.from_bytes(d, byteorder='little') for d in x]

def cvt2_string_buffer(xs:list) -> 'c_char*int':
    
    return 

from ctypes import create_string_buffer
x0 = [1, 0, 2]
xs = create_string_buffer(bytes(x0), len(x0))
x1 = [int.from_bytes(d, byteorder='little') for d in xs]

print(x1) # [1, 0, 2, 0]
