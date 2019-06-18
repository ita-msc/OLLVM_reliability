#!/usr/bin/python3
import sys
import r2pipe
import json


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This script intends to determine, thanks to the output data it generates, the most significant features to use in the radare2Analysis_&_OutputSkimming.py and then scoring.py scripts.
# The output data generated is a csv formatted file providing, for the program specified in the parameter, the list of the functions called by it and their features (size, cost, calltype, nargs,
# nargs, etc)
#
# PROTOCOL:
# To run this program the command line is : python3 radare2_Output_Processing.py [executable file]
# Thanks to a 'for' loop written in bash, we ran this "json-to-csv-converter" script for each benchmarcksgame program (C, C++).
# The benchmarksgames programs used for this features analysis can be found at: https://github.com/ita-msc/OLLVM_reliability/tree/master/OLLVM_reliability/benchmark_samples
# 
# RESULT of the csv file analysis:
# Some features turn out to be relevant for both the "skimming phase" and the scoring phase.
# Indeed, in an effort to have the least bias in the final score, we set up a "skimming phase" before the scoring one. [see radare2Analysis_&_OutputSkimming.py]
# The relevant features seem to be, for a function called by the input program: size, nbbs, the number of jumps (cref_J), datarefsNb, the ratios size/nbbs and cref_J/nbbs .
# In fact, these selected characteristics could be good indicators when assessing whether and to what extent a program is obscured.  
# In short, the more a program is obfuscated, the more nbbs (number of basic blocs) it has, so the bigger it sould be. The number of jumps is also important as the obfuscation impacts the
# workflow of a program.
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




################################################## USER SECTION #######################################################
# Choose the analysis and listing commands you want to apply to the input file (NO NEED TO CHANGE THESE)
ANALYSIS_CMD        = "aa"
LISTING_CMD         = "aflj~{}"     # does'nt work with another non json formatted command for the moment
SEPARATOR           = "!"           # don't use "," or "/"
#######################################################################################################################





# opening the input executable file
r2 = r2pipe.open(str(sys.argv[1])) 



# basic analysis and listing the functions commands
r2.cmd(ANALYSIS_CMD)
radare2_output = r2.cmd(LISTING_CMD)



# loading and processing the json output
# loading json output
radare2_output_json           = json.loads(radare2_output.decode("utf-8")) 
radare2_output_lines_number   = len(radare2_output_json)


# printing relevant data from json output in csv format
columnTitleRow = "programName" + SEPARATOR + "calltype" + SEPARATOR + "realsz" + SEPARATOR + "name"+ SEPARATOR + "cc"+ SEPARATOR + "indegree"+ SEPARATOR + "nargs"+ SEPARATOR + "edges"+ SEPARATOR + "outdegree"+ SEPARATOR + "cost"+ SEPARATOR + "nlocals"+ SEPARATOR + "offset"+ SEPARATOR + "ebbs" + SEPARATOR + "nbbs"+ SEPARATOR + "type"+ SEPARATOR + "size"+ SEPARATOR + "datarefsNb" + SEPARATOR + "cref_c" + SEPARATOR + "cref_j"+ SEPARATOR + "diff"+ SEPARATOR + "difftype"
print (columnTitleRow)

for line in range(radare2_output_lines_number):       # for each line in the json output, which represents each function in the program, print some data about it
    print(str(sys.argv[1]), end='')
    print(SEPARATOR + str(radare2_output_json[line]['calltype']), end='')
    print(SEPARATOR + str(radare2_output_json[line]['realsz']), end='')
    print(SEPARATOR + str(radare2_output_json[line]['name']), end='')
    print(SEPARATOR + str(radare2_output_json[line]['cc']), end='')
    print(SEPARATOR + str(radare2_output_json[line]['indegree']), end='')
    print(SEPARATOR + str(radare2_output_json[line]['nargs']), end='')
    print(SEPARATOR + str(radare2_output_json[line]['edges']), end='')
    print(SEPARATOR + str(radare2_output_json[line]['outdegree']), end='')
    print(SEPARATOR + str(radare2_output_json[line]['cost']), end='')
    print(SEPARATOR + str(radare2_output_json[line]['nlocals']), end='')
    print(SEPARATOR + str(radare2_output_json[line]['offset']), end='')
    print(SEPARATOR + str(radare2_output_json[line]['ebbs']), end='')
    print(SEPARATOR + str(radare2_output_json[line]['nbbs']), end='')
    print(SEPARATOR + str(radare2_output_json[line]['type']), end='')
    print(SEPARATOR + str(radare2_output_json[line]['size']), end='')

    if 'datarefs' in radare2_output_json[line].keys():
        print(SEPARATOR + str(len(radare2_output_json[line]['datarefs'])), end='') # print the number of datarefs (offsets) 

    if 'datarefs' not in radare2_output_json[line].keys():  # it happens that there is no 'datarefs' key. 
                                                            # In that case, we make sure not to leave a blank space that could be filled by a value of another key (offset in the csv)
        print (SEPARATOR + "EMPTY", end='')

    if 'callrefs' in radare2_output_json[line].keys():
        if len(radare2_output_json[line]['callrefs'])== 0:
            print(SEPARATOR + "NOCALLREF", end='')
            print(SEPARATOR + "NOCALLREF", end='')
        else:
            print (SEPARATOR, end='')
            J_count = 0
            C_count = 0
            for elt in range(len(radare2_output_json[line]['callrefs'])): 
                if radare2_output_json[line]['callrefs'][elt]['type'] == "C":
                    C_count+=1
                if radare2_output_json[line]['callrefs'][elt]['type'] == "J":
                    J_count+=1
            print (str(C_count), end='')         # print the number of calls of another function per function
            print (SEPARATOR + str(J_count), end='')         # print the number of jump to another memory space per function
    
    if 'callrefs' not in radare2_output_json[line].keys():
        print (SEPARATOR + "NOCALLREF", end='')
        print(SEPARATOR + "NOCALLREF", end='')

    if 'diff' in radare2_output_json[line].keys():
        print(SEPARATOR + str(radare2_output_json[line]['diff']), end='')

    if 'diff' not in radare2_output_json[line].keys():    # it happens that there is no 'diff' key. for function which the name starts with "loc". So same treatment as above.
        print (SEPARATOR + " ", end='')

    if 'difftype' in radare2_output_json[line].keys():    # it happens that there is no 'difftype' key. for function which the name starts with "loc". So same treatment as above.
        print(SEPARATOR + str(radare2_output_json[line]['difftype']))
 
    else:
        print(" ")