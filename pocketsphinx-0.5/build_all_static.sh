#!/bin/sh

cd sphinxbase
mkdir inst
./configure --prefix=`pwd`/inst --disable-shared --without-lapack --without-python
make

cd ../pocketsphinx
mkdir inst
./configure --prefix=`pwd`/inst --disable-shared --without-python --with-sphinxbase=`pwd`/../sphinxbase
make install
