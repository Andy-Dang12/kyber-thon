#! /bin/bash
cur=$(pwd)
cd $(dirname "$(readlink -f "$0")")
cd ../ref
make shared
cd ..
cd "$cur"
