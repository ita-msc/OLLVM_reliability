#!/usr/bin/python3
import sys
import r2pipe
import json
import os
from itertools import repeat
import csv


# ------------------------------------------------------------------------------------------------------------------------------------
# This script intends to decide, thanks to the output data it generates, which sorting criterion to use in the radar2_analysis-v2.py 
# ------------------------------------------------------------------------------------------------------------------------------------

################################################## USER SECTION #######################################################
# Choose the analysis and listing commands you want to apply to the input file
ANALYSIS_CMD        = "aa"
LISTING_CMD         = "aflj~{}"
SEPARATOR           = "§"
#######################################################################################################################



# opening the input executable file
# print("Opening the input executable file")
r2 = r2pipe.open(str(sys.argv[1])) 



# basic analysis and listing commands
r2.cmd(ANALYSIS_CMD)
aflj_output = r2.cmd(LISTING_CMD)



# loading and processing the json output
# print("Loading and processing the json output...")
aflj_json           = json.loads(aflj_output.decode()) #ici il faut rajouter un .decode() qqch
aflj_lines_number   = len(aflj_json)
# print (aflj_json)




columnTitleRow = "programName" + SEPARATOR + "calltype" + SEPARATOR + "realsz" + SEPARATOR + "name"+ SEPARATOR + "cc"+ SEPARATOR + "indegree"+ SEPARATOR + "nargs"+ SEPARATOR + "edges"+ SEPARATOR + "outdegree"+ SEPARATOR + "cost"+ SEPARATOR + "nlocals"+ SEPARATOR + "offset"+ SEPARATOR + "ebbs" + SEPARATOR + "nbbs"+ SEPARATOR + "type"+ SEPARATOR + "size"+ SEPARATOR + "datarefsNb" + SEPARATOR + "cref_c" + SEPARATOR + "cref_j"+ SEPARATOR + "diff"+ SEPARATOR + "difftype"
print (columnTitleRow)
for line in range(aflj_lines_number):
    print(str(sys.argv[1]), end='')
    print (SEPARATOR, end='')
    print (aflj_json[line]['calltype'], end='')
    print (SEPARATOR, end='')
    print(aflj_json[line]['realsz'], end='')
    print (SEPARATOR, end='')
    print(aflj_json[line]['name'], end='')
    print (SEPARATOR, end='')
    print(aflj_json[line]['cc'], end='')
    print (SEPARATOR, end='')
    print(aflj_json[line]['indegree'], end='')
    print (SEPARATOR, end='')
    print(aflj_json[line]['nargs'], end='')
    print (SEPARATOR, end='')
    print(aflj_json[line]['edges'], end='')
    print (SEPARATOR, end='')
    print(aflj_json[line]['outdegree'], end='')
    print (SEPARATOR, end='')
    print(aflj_json[line]['cost'], end='')
    print (SEPARATOR, end='')
    print(aflj_json[line]['nlocals'], end='')
    print (SEPARATOR, end='')
    print(aflj_json[line]['offset'], end='')
    print (SEPARATOR, end='')
    print(aflj_json[line]['ebbs'], end='')
    print (SEPARATOR, end='')
    print(aflj_json[line]['nbbs'], end='')
    print (SEPARATOR, end='')
    print(aflj_json[line]['type'], end='')
    print (SEPARATOR, end='')
    print(aflj_json[line]['size'], end='')

    if 'datarefs' in aflj_json[line].keys():
        print (SEPARATOR, end='')
        print(len(aflj_json[line]['datarefs']), end='')

    if 'datarefs' not in aflj_json[line].keys():
        print (SEPARATOR, end='')
        print ("EMPTY", end='')

    if 'callrefs' in aflj_json[line].keys():
        if len(aflj_json[line]['callrefs'])== 0:
            print (SEPARATOR, end='')
            print("NOCALLREF", end='')
            print( SEPARATOR, end='')
            print("NOCALLREF", end='')
        else:
            print (SEPARATOR, end='')
            J_count = 0
            C_count = 0
            for elt in range(len(aflj_json[line]['callrefs'])): 
                if aflj_json[line]['callrefs'][elt]['type'] == "C":
                    C_count+=1
                if aflj_json[line]['callrefs'][elt]['type'] == "J":
                    J_count+=1
            print (C_count, end='')
            print(SEPARATOR, end='')
            print (J_count, end='')
    
    if 'callrefs' not in aflj_json[line].keys():
        print (SEPARATOR, end='')
        print ("NOCALLREF", end='')
        print( SEPARATOR, end='')
        print("NOCALLREF", end='')

    if 'diff' in aflj_json[line].keys():
        print (SEPARATOR, end='')
        print(aflj_json[line]['diff'], end='')

    if 'diff' not in aflj_json[line].keys():
        print (SEPARATOR, end='')
        print (" ", end='')

    if 'difftype' in aflj_json[line].keys():
        print (SEPARATOR, end='')
        print(aflj_json[line]['difftype'])
 
    else:
        print(" ")
   
