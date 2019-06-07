#!/bin/bash

echo "PHASE ONE -------> Compiling..."


#[[ ! -d benchmark_samples_compiled ]] && mkdir benchmark_samples_compiled
#[[ -d benchmark_samples_compiled ]] || mkdir benchmark_samples_compiled
#if [[ ! -d benchmark_samples_compiled ]] ; then 
#
# else
#
#fi

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

cd ./benchmark_samples
git clone https://www.bearssl.org/git/BearSSL
cd BearSSL
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

clang++ -I/usr/include/re2 -O0 ./benchmark_samples/regexdna.cpp -o ./benchmark_samples_compiled/regexdna.o0 -L/usr/include/re2 -lre2 -Xlinker -rpath=/usr/include/re2
clang++ -I/usr/include/re2 -O0 ./benchmark_samples/regexdna.cpp -o ./benchmark_samples_compiled/regexdna.o0.fla.sub.bcf -L/usr/include/re2 -lre2 -Xlinker -rpath=/usr/include/re2 -mllvm -fla -mllvm -sub -mllvm -bcf
echo "compiled 9/10"

clang++ -I/opt/boost -O0 ./benchmark_samples/knucleotide.cpp -o ./benchmark_samples_compiled/knucleotide.o0 -L/opt/boost/stage/lib -lpthread -Xlinker -rpath=/opt/boost/stage/lib -lomp
clang++ -I/opt/boost -O0 ./benchmark_samples/knucleotide.cpp -o ./benchmark_samples_compiled/knucleotide.o0.fla.sub.bcf -L/opt/boost/stage/lib -lpthread -Xlinker -rpath=/opt/boost/stage/lib -lomp -mllvm -fla -mllvm -sub -mllvm -bcf
echo "compiled 10/10"

echo "PHASE ONE Done. A benchmark_samples_compiled directory has just been created. Check it out! "

echo "PHASE TWO -------> Analyzing compiled files..."


# for f in $(find . -name "*.o0*" -executable | grep "bmg_") # changer le bmg machin
# do
#   echo $f
#   python3 bmg_meteor/minitest.py $f >> bmg_radare2_data_MINITEST.csv
# done
