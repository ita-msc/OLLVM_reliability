#!/bin/bash

echo "compiling..."


mkdir benchmark_samples_compiled


clang++ -O0 ./benchmark_samples/threadring.cpp -o ./benchmark_samples_compiled/threadring.o0 -pthread
clang++ -O0 ./benchmark_samples/threadring.cpp -o ./benchmark_samples_compiled/threadring.o0.fla.sub.bcf -pthread -mllvm -fla -mllvm -sub -mllvm -bcf
echo "compiled 1/10"

clang++ -O0 ./benchmark_samples/fastaredux.cpp -o ./benchmark_samples_compiled/fastaredux.o0
clang++ -O0 ./benchmark_samples/fastaredux.cpp -o ./benchmark_samples_compiled/fastaredux.o0.fla.sub.bcf -mllvm -fla -mllvm -sub -mllvm -bcf
echo "compiled 2/10" 

clang++ -O0 ./benchmark_samples/meteor.cpp -o ./benchmark_samples_compiled/meteor.o0
clang++ -O0 ./benchmark_samples/meteor.cpp -o ./benchmark_samples_compiled/meteor.o0.fla.sub.bcf -mllvm -fla -mllvm -sub -mllvm -bcf
echo "compiled 3/10"

clang -O0 ./benchmark_samples/fannkuchredux.c -o ./benchmark_samples_compiled/fannkuchredux.o0
clang -O0 ./benchmark_samples/fannkuchredux.c -o ./benchmark_samples_compiled/fannkuchredux.o0.fla.sub.bcf -mllvm -fla -mllvm -bcf -mllvm -sub
echo "compiled 4/10"

clang++ -O0 ./benchmark_samples/spectralnorm.cpp -o ./benchmark_samples_compiled/spectralnorm.o0
clang++ -O0 ./benchmark_samples/spectralnorm.cpp -o ./benchmark_samples_compiled/spectralnorm.o0.fla.sub.bcf -mllvm -fla -mllvm -bcf -mllvm -sub
echo "compiled 5/10"

cd ./benchmark_samples/BearSSL
make CONF=UnixClang CFLAGS='-O0 -fPIC'
mv ./bclang/libbearssl.so ../../benchmark_samples_compiled/libbearssl.o0.so
rm -r bclang
make CONF=UnixClang CFLAGS='-mllvm -fla -mllvm -sub -mllvm -bcf -O0 -fPIC'
cp ./bclang/libbearssl.so ../../benchmark_samples_compiled/libbearssl.o0.fla.sub.bcf.so
cd ../..
echo "compiled 6/10"

clang -I/usr/include/x86_64-linux-gnu ./benchmark_samples/pidigits.c -o ./benchmark_samples_compiled/pidigits.o0 -lgmp
clang -I/usr/include/x86_64-linux-gnu ./benchmark_samples/pidigits.c -o ./benchmark_samples_compiled/pidigits.o0.fla.sub.bcf -lgmp -mllvm -fla -mllvm -sub -mllvm -bcf
echo "compiled 7/10"

clang++ -O0 ./benchmark_samples/revcomp.cpp -o ./benchmark_samples_compiled/revcomp.o0
clang++ -O0 ./benchmark_samples/revcomp.cpp -o ./benchmark_samples_compiled/revcomp.o0.fla.sub.bfc -mllvm -fla -mllvm -bcf -mllvm -sub
echo "compiled 8/10"


echo "Done. A benchmark_samples_compiled directory has just been created. Check it out! "