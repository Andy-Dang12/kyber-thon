from os.path import abspath, join
from ctypes import cdll, c_int, c_ubyte, POINTER


fips202_ref  = cdll.LoadLibrary(abspath(join(
    __file__, '..', '..', '..', 'ref/libpqcrystals_fips202_ref.so')))

#* sha3_256
pqcrystals_kyber_fips202_ref_sha3_256 = fips202_ref.pqcrystals_kyber_fips202_ref_sha3_256
pqcrystals_kyber_fips202_ref_sha3_256.restype = None
pqcrystals_kyber_fips202_ref_sha3_256.argtypes = []


#*sha3_512
pqcrystals_kyber_fips202_ref_sha3_512 = fips202_ref.pqcrystals_kyber_fips202_ref_sha3_512
pqcrystals_kyber_fips202_ref_sha3_512.restype = None
pqcrystals_kyber_fips202_ref_sha3_512.argtypes = []



pqcrystals_kyber_fips202_ref_shake128 = fips202_ref.pqcrystals_kyber_fips202_ref_shake128
pqcrystals_kyber_fips202_ref_shake128.restype = None
pqcrystals_kyber_fips202_ref_shake128.argtypes = []




pqcrystals_kyber_fips202_ref_shake128_absorb = fips202_ref.pqcrystals_kyber_fips202_ref_shake128_absorb
pqcrystals_kyber_fips202_ref_shake128_absorb.restype = None
pqcrystals_kyber_fips202_ref_shake128_absorb.argtypes = []



pqcrystals_kyber_fips202_ref_shake128_absorb_once = fips202_ref.pqcrystals_kyber_fips202_ref_shake128_absorb_once
pqcrystals_kyber_fips202_ref_shake128_absorb_once.restype = None
pqcrystals_kyber_fips202_ref_shake128_absorb_once.argtypes = []



pqcrystals_kyber_fips202_ref_shake128_finalize = fips202_ref.pqcrystals_kyber_fips202_ref_shake128_finalize
pqcrystals_kyber_fips202_ref_shake128_finalize.restype = None
pqcrystals_kyber_fips202_ref_shake128_finalize.argtypes = []



pqcrystals_kyber_fips202_ref_shake128_init = fips202_ref.pqcrystals_kyber_fips202_ref_shake128_init
pqcrystals_kyber_fips202_ref_shake128_init.restype = None
pqcrystals_kyber_fips202_ref_shake128_init.argtypes = []



pqcrystals_kyber_fips202_ref_shake128_squeeze = fips202_ref.pqcrystals_kyber_fips202_ref_shake128_squeeze
pqcrystals_kyber_fips202_ref_shake128_squeeze.restype = None
pqcrystals_kyber_fips202_ref_shake128_squeeze.argtypes = []



pqcrystals_kyber_fips202_ref_shake128_squeezeblocks = fips202_ref.pqcrystals_kyber_fips202_ref_shake128_squeezeblocks
pqcrystals_kyber_fips202_ref_shake128_squeezeblocks.restype = None
pqcrystals_kyber_fips202_ref_shake128_squeezeblocks.argtypes = []



pqcrystals_kyber_fips202_ref_shake256 = fips202_ref.pqcrystals_kyber_fips202_ref_shake256
pqcrystals_kyber_fips202_ref_shake256.restype = None
pqcrystals_kyber_fips202_ref_shake256.argtypes = []



pqcrystals_kyber_fips202_ref_shake256_absorb = fips202_ref.pqcrystals_kyber_fips202_ref_shake256_absorb
pqcrystals_kyber_fips202_ref_shake256_absorb = None
pqcrystals_kyber_fips202_ref_shake256_absorb.argtypes = []



pqcrystals_kyber_fips202_ref_shake256_absorb_once   = fips202_ref.pqcrystals_kyber_fips202_ref_shake256_absorb_once
pqcrystals_kyber_fips202_ref_shake256_absorb_once
pqcrystals_kyber_fips202_ref_shake256_absorb_once.argtypes = []



pqcrystals_kyber_fips202_ref_shake256_finalize      = fips202_ref.pqcrystals_kyber_fips202_ref_shake256_finalize
pqcrystals_kyber_fips202_ref_shake256_finalize
pqcrystals_kyber_fips202_ref_shake256_finalize.argtypes = []



pqcrystals_kyber_fips202_ref_shake256_init          = fips202_ref.pqcrystals_kyber_fips202_ref_shake256_init
pqcrystals_kyber_fips202_ref_shake256_init
pqcrystals_kyber_fips202_ref_shake256_init.argtypes = []



pqcrystals_kyber_fips202_ref_shake256_squeeze       = fips202_ref.pqcrystals_kyber_fips202_ref_shake256_squeeze
pqcrystals_kyber_fips202_ref_shake256_squeeze
pqcrystals_kyber_fips202_ref_shake256_squeeze.argtypes = []



pqcrystals_kyber_fips202_ref_shake256_squeezeblocks = fips202_ref.pqcrystals_kyber_fips202_ref_shake256_squeezeblocks
pqcrystals_kyber_fips202_ref_shake256_squeezeblocks
pqcrystals_kyber_fips202_ref_shake256_squeezeblocks.argtypes = []
