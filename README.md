# OLLVM_reliability


*OLLVM_reliability* is a project that aims to provide suppport to the developpers of [OLLVM](https://github.com/ita-msc/obfuscator), an open source obfuscator.

When a modification on OLLVM is pushed, this project will automatically be triggered and start the assessment of the latest OLLVM version. At the end of the evaluation, a score is provided to developers as a reliability indicator, which will be tracked over time with each version of ollvm.
<br/>

### How it works, the assessment protocol:
A given OLLVM version is evaluated according to this three-phases protocol:
1) A sample of various programs are compiled with and without obfuscation. The compiler of OLLVM is called Clang.
2) The **compiling** phase is then followed by the **analysis** one. The output thus obtained is filtered before giving a score. 
3) The **scoring** phase is the last one and provides the final reliability indicator for the given OLLVM version.
![assessment protocole](Docs/assessment_protocol.png)
<br/>


### How it is organized:
* __```allthejob.bash```:__ does the compiling phase, and calls the useful python scripts for both the analysis and the scoring phases. 
It invokes the following scripts:  
    * ```radare2Analysis_Filtering_and_Scoring.py```
    * ```scoring.py```
    * ```finalScoresCollector.py```
    * ```averageScores.py```
<br/>

* __```radare2Analysis_Filtering_and_Scoring.py```:__ gets a compiled program and analyses it with [radare2](https://github.com/radare/radare2). radare2 provides a large amount of data about each function called in the program. This script sorts the data from a scoring formula which may evolve and can easily be changed. The only line to be modified in this script is the following one: 
```python 
SCORING_FORMULA     = (line['realsz']/line['nbbs']) * J_count
```
Then, the filtered set of data is sent to the ```scoring.py``` script.
<br/>

* __```scoring.py```:__ calculates an average score for each program, whether it is obfuscated or not, and returns two average scores: one for the obfuscated programs and another one for the non obfuscated ones. The output file then contains a detailed overview of all scores per programs, and two average scores.
<br/>

* __```finalScoresCollector.py```:__ gathers all obfuscated average scores and non-obfuscated average scores obtained after running the assessment protocol i times. This script will, in the same way as ```scoring.py```, calculate two averages (obfuscated and non obfuscated) from the i scores.
<br/>

* __```/benchmak_samples```__: contains the source code of the programs that will be compiled with the assessed version of ollvm.
<br/>

The other programs in the /OLLVM_reliability folder represent the track of the work done before reaching the current version:

* __```radare2OutputFormatting.py```:__ converts the output data provided by radare2, which is json formatted into csv format. On top of that, the script digs through the data and extracts some other pieces of information judged relevant (number of jumps, callrefs, etc). Having a view of the data in excel format allowed us to decide which on which feature (size of the function, cost, number of basic blocks, etc) our scoring formula will be based. 
* __```radare2Analysis_and_OutputFiltering-v1/2.py```:__ both represent the first implementations of the radare2 analysis and the output filtering which have not been retained.
* __```performanceAnalysis.py```:__ is a script ready to welcome an implementation of a performance indicator that will help the OLLVM developpers understand the effects of obfuscation on the performance of a program.
<br/>

### How to use _OLLVM_reliability_:

#### Prerequisite

Few dependencies are needed in order to comile the samples :
```bash
sudo apt -y install python3 python3-pip libre2-dev libomp-dev libgmp-dev libgmp3-dev radare2
```
As well, r2pipe module is needed for the scripts:
```bash
pip3 install r2pipe
```

#### Use it

The main prerequisite to make this project work and be able to use it is having a version of OLLVM installed. 
You also have to make sure that the version used during the compiling phase is not the default one but the one you previously installed.
You can run the following command to find out the current version of clang:
```bash
which clang
```
<br/>

After cloning the _OLLVM_reliability_ project, the only command you need to run is:
```bash
bash allthejob.bash
```
The expected output should look like:
![expected_screenshot](Docs/screenshot_mdreadme.PNG)
<br/>

### What is worth reviewing/ways to improve:
* __The number and variety of programms in /benchmark_samples:__ The more programs you have tested by the compiler, the better. What is more, adding Objective-C programs in this sample may be a good way to make the sample more complete. 
<br/>

* __The scoring formula:__ Many scoring formulas have been tested, but none of them really  stood out from the crowd. As the scoring formula is what provides the final reliability indicator to the OLLVM developpers, we must consider this part seiously.
<br/>

* __The influence of obfuscation on the performance:__ In order to further this assessment protocol, we may consider the effet of obfuscation on the performance of a program.


<br/>

### Contributors:
Anaïs NALEM, 4th-year student at INSA Centre Val de Loire contributed from April to July 2019
