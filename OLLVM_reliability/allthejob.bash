#!/bin/bash

ollvm_version="7.0.1" # get it from the .gitlab file or smth like this

set -e

#  Name the scoring details file with the tested ollvm-version
if [ -z "$ollvm_version" ];
    then
        scoringdetails="scoringdetails_DEFAULT"
    fi

if ! [ -z "$ollvm_version" ];
    then
        scoringdetails="scoringdetails_${ollvm_version}"
    fi

rm -rf ./benchmark_samples_compiled ./scoringresults_${ollvm_version} ./benchmark_samples/BearSSL

#   As obfuscation brings incertitude to the code, and thus offers variations in the score of a same program,
#   we run the ollvm assessment protocole many times to then calculate an average of the obtained scores.
for i in {1..3} # you can change the number of iterations here!!
do 
    mkdir ./benchmark_samples_compiled/
    mkdir -p ./scoringresults_${ollvm_version}/

    echo "PHASE ONE -------> Compiling..."
    clang++ -O0 ./benchmark_samples/threadring.cpp -o ./benchmark_samples_compiled/threadring.o0 -pthread
    clang++ -O0 ./benchmark_samples/threadring.cpp -o ./benchmark_samples_compiled/threadring.o0.fla.sub.bcf -pthread -mllvm -fla -mllvm -sub -mllvm -bcf
    echo "compiling 1/10"

    clang++ -O0 ./benchmark_samples/fastaredux.cpp -o ./benchmark_samples_compiled/fastaredux.o0
    clang++ -O0 ./benchmark_samples/fastaredux.cpp -o ./benchmark_samples_compiled/fastaredux.o0.fla.sub.bcf -mllvm -fla -mllvm -sub -mllvm -bcf
    echo "compiling 2/10" 

    clang++ -O0 ./benchmark_samples/meteor.cpp -o ./benchmark_samples_compiled/meteor.o0
    clang++ -O0 ./benchmark_samples/meteor.cpp -o ./benchmark_samples_compiled/meteor.o0.fla.sub.bcf -mllvm -fla -mllvm -sub -mllvm -bcf
    echo "compiling 3/10"

    clang -O0 ./benchmark_samples/fannkuchredux.c -o ./benchmark_samples_compiled/fannkuchredux.o0
    clang -O0 ./benchmark_samples/fannkuchredux.c -o ./benchmark_samples_compiled/fannkuchredux.o0.fla.sub.bcf -mllvm -fla -mllvm -bcf -mllvm -sub
    echo "compiling 4/10"

    clang++ -O0 ./benchmark_samples/spectralnorm.cpp -o ./benchmark_samples_compiled/spectralnorm.o0
    clang++ -O0 ./benchmark_samples/spectralnorm.cpp -o ./benchmark_samples_compiled/spectralnorm.o0.fla.sub.bcf -mllvm -fla -mllvm -bcf -mllvm -sub
    echo "compiling 5/10"

    cd ./benchmark_samples
    git clone https://www.bearssl.org/git/BearSSL
    cd BearSSL
    make CONF=UnixClang CFLAGS='-O0 -fPIC'
    mv ./bclang/libbearssl.so ../../benchmark_samples_compiled/libbearssl.o0.so
    rm -r bclang
    make CONF=UnixClang CFLAGS='-mllvm -fla -mllvm -sub -mllvm -bcf -O0 -fPIC'
    cp ./bclang/libbearssl.so ../../benchmark_samples_compiled/libbearssl.o0.fla.sub.bcf.so
    cd ../..
    echo "compiling 6/10"

    clang -I/usr/include/x86_64-linux-gnu ./benchmark_samples/pidigits.c -o ./benchmark_samples_compiled/pidigits.o0 -lgmp
    clang -I/usr/include/x86_64-linux-gnu ./benchmark_samples/pidigits.c -o ./benchmark_samples_compiled/pidigits.o0.fla.sub.bcf -lgmp -mllvm -fla -mllvm -sub -mllvm -bcf
    echo "compiling 7/10"

    clang++ -O0 ./benchmark_samples/revcomp.cpp -o ./benchmark_samples_compiled/revcomp.o0
    clang++ -O0 ./benchmark_samples/revcomp.cpp -o ./benchmark_samples_compiled/revcomp.o0.fla.sub.bfc -mllvm -fla -mllvm -bcf -mllvm -sub
    echo "compiling 8/10"

    clang++ -I/usr/include/re2 -O0 ./benchmark_samples/regexdna.cpp -o ./benchmark_samples_compiled/regexdna.o0 -L/usr/include/re2 -lre2 -Xlinker -rpath=/usr/include/re2
    clang++ -I/usr/include/re2 -O0 ./benchmark_samples/regexdna.cpp -o ./benchmark_samples_compiled/regexdna.o0.fla.sub.bcf -L/usr/include/re2 -lre2 -Xlinker -rpath=/usr/include/re2 -mllvm -fla -mllvm -sub -mllvm -bcf
    echo "compiling 9/10"

    clang++ -I/opt/boost -O0 ./benchmark_samples/knucleotide.cpp -o ./benchmark_samples_compiled/knucleotide.o0 -L/opt/boost/stage/lib -lpthread -Xlinker -rpath=/opt/boost/stage/lib -lomp
    clang++ -I/opt/boost -O0 ./benchmark_samples/knucleotide.cpp -o ./benchmark_samples_compiled/knucleotide.o0.fla.sub.bcf -L/opt/boost/stage/lib -lpthread -Xlinker -rpath=/opt/boost/stage/lib -lomp -mllvm -fla -mllvm -sub -mllvm -bcf
    echo "compiling 10/10"

    echo "PHASE ONE Done. A benchmark_samples_compiled directory has just been created. Check it out! "
    
    
    echo "PHASE TWO -------> Analyzing compiled files..."
 
    cd ./scoringresults_${ollvm_version}/   # this folder will contains i files named as following
    touch ${scoringdetails}-${i}.csv        # these files will contains the score for both obfuscated and non obfuscated programs and two average scores (obfuscated and non obfuscated)
    echo "Program name,Score" > ${scoringdetails}-${i}.csv
    cd ..


    for f in ./benchmark_samples_compiled/*.o0*
    do
        echo $f
        python3 radare2Analysis_Filtering_and_Scoring.py $f >> ./scoringresults_${ollvm_version}/${scoringdetails}-${i}.csv #peut etre mettre le nom de la version de ollvm dans le nom du fichier resultat
    done



    echo "PHASE THREE -------> Calculating the final average score..."

    python3 scoring.py ./scoringresults_${ollvm_version}/${scoringdetails}-${i}.csv >> ./scoringresults_${ollvm_version}/${scoringdetails}-${i}.csv

    rm -rf ./benchmark_samples_compiled ./benchmark_samples/BearSSL
done



echo " A final score for ollvm_v${ollvm_version} has been calculated ${i} times. It's time to calculate an avarage of these final scores."


cd ./scoringresults_${ollvm_version}/
touch finalscores-${ollvm_version}.csv  #   this file will contain i lines for each final scores, obfuscated and non obfuscated, and two average scores (obfuscated and non obfuscated) to have the final scores for the assessed ollvm version
echo "Obfuscated scores, Non obfuscated scores" > finalscores-${ollvm_version}.csv
cd ..

for f in ./scoringresults_${ollvm_version}/*.csv
do
    python3 finalScoresCollector.py $f >> ./scoringresults_${ollvm_version}/finalscores-${ollvm_version}.csv
done

python3 averageScores.py ./scoringresults_${ollvm_version}/finalscores-${ollvm_version}.csv >> ./scoringresults_${ollvm_version}/finalscores-${ollvm_version}.csv

echo "Everything is done. You can find a detail of the scores in ./scoringresults_${ollvm_version}/ folder."
echo "Here are the final scores:"
cat ./scoringresults_${ollvm_version}/finalscores-${ollvm_version}.csv