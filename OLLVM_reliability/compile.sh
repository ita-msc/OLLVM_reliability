#!/bin/bash

echo "compiling..."


mkdir benchmark_samples_compiled

clang++ -O0 ./benchmark_samples/threadring.cpp -o ./benchmark_samples_compiled/threadring.o0 -pthread
clang++ -O0 ./benchmark_samples/threadring.cpp -o ./benchmark_samples_compiled/threadring.o0.fla.sub.bcf -pthread -mllvm -fla -mllvm -sub -mllvm -bcf
echo "compiled 1/10 programs"

clang++ -I/opt/boost -o0 ./benchmark_samples/chameneosredux.cpp -o ./benchmark_samples_compiled/chameneosredux.o0 -L/opt/boost/stage/lib -lboost_thread -lpthread -Xlinker -rpath=/opt/boost/stage/lib
echo "compiled 2/10 programs"

clang++ -O0 ./benchmark_samples/fastaredux.cpp -o ./benchmark_samples_compiled/fastaredux.o0
clang++ -O0 ./benchmark_samples/fastaredux.cpp -o ./benchmark_samples_compiled/fastaredux.o0.fla.sub.bcf -mllvm -fla -mllvm -sub -mllvm -bcf
echo "compiled 3/10 programs" 

clang++ -O0 ./benchmark_samples/meteor.cpp -o ./benchmark_samples_compiled/meteor.o0
clang++ -O0 ./benchmark_samples/meteor.cpp -o ./benchmark_samples_compiled/meteor.o0.fla.sub.bcf -mllvm -fla -mllvm -sub -mllvm -bcf
echo "compiled 4/10 programs"

clang -O0 ./benchmark_samples/fannkuchredux.c -o ./benchmark_samples_compiled/fannkuchredux.o0
clang -O0 ./benchmark_samples/fannkuchredux.c -o ./benchmark_samples_compiled/fannkuchredux.o0.fla.sub.bcf -mllvm -fla -mllvm -bcf -mllvm -sub
echo "compiled 5/10 programs"

clang++ -O0 ./benchmark_samples/spectralnorm.cpp -o ./benchmark_samples_compiled/spectralnorm.o0
clang++ -O0 ./benchmark_samples/spectralnorm.cpp -o ./benchmark_samples_compiled/spectralnorm.o0.fla.sub.bcf -mllvm -fla -mllvm -bcf -mllvm -sub
echo "compiled 6/10 programs"

echo "Done. A benchmark_samples_compiled directory has just been created. Check it out! "