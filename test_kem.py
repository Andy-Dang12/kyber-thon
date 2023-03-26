import numpy as np

from kython.pqc_kyber512_ref import (
    pqc_kyber512_ref_keypair as keypair,
    pqc_kyber512_ref_enc     as encode,
    pqc_kyber512_ref_dec     as decode
)
key_b = [72, 101, 108, 108, 111] * 6 + [72, 101]


pk, sk = keypair()
ct = encode(key_b, pk)
key_a = decode(ct, sk)

print(key_a)
print(key_b)
# assert key_a == key_b