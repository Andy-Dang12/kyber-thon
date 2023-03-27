#! /bin/bash
cur=$(pwd)
cd $(dirname "$(readlink -f "$0")")
cd ../ref
# make shared
# rm libpqcrystals_kyber512_ref.so
# make libpqcrystals_kyber512_ref.so

make test_kyber512
cd ..
cd "$cur"
