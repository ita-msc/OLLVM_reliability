#!/usr/bin/python3
import sys
import r2pipe
import json
import os

# ------------------------------------------------------------------------------------------------------------------------------------
# This script intends to decide, thanks to the output data it generates, which sorting criterion to use in the radar2_analysis-v2.py 
# ------------------------------------------------------------------------------------------------------------------------------------

################################################## USER SECTION #######################################################
# Choose the analysis and listing commands you want to apply to the input file
ANALYSIS_CMD        = "aa"
LISTING_CMD         = "aflj~{}"
#######################################################################################################################



# opening the input executable file
r2 = r2pipe.open(str(sys.argv[1])) 



# basic analysis and listing commands
r2.cmd(ANALYSIS_CMD)
aflj_output = r2.cmd(LISTING_CMD)



# loading and processing the json output
print("Loading and processing the json output...")
aflj_json           = json.loads(aflj_output)
aflj_lines_number   = len(aflj_json)

columnTitleRow = "programName,calltype,realsz,diff,name,cc,indegree,nargs,difftype,edges,outdegree,cost,nlocals,offset,ebbs,nbbs,type,size,datarefsNb,cref_c,cref_j\n"
print (columnTitleRow)
for line in range(aflj_lines_number):
    print(str(sys.argv[1]), end='')
    print (",", end='')
    print (aflj_json[line]['calltype'], end='')
    print (",", end='')
    print(aflj_json[line]['realsz'], end='')
    print (",", end='')
    print(aflj_json[line]['diff'], end='')
    print (",", end='')
    print(aflj_json[line]['name'], end='')
    print (",", end='')
    print(aflj_json[line]['cc'], end='')
    print (",", end='')
    print(aflj_json[line]['indegree'], end='')
    print (",", end='')
    print(aflj_json[line]['nargs'], end='')
    print (",", end='')
    print(aflj_json[line]['difftype'], end='')
    print (",", end='')
    print(aflj_json[line]['edges'], end='')
    print (",", end='')
    print(aflj_json[line]['outdegree'], end='')
    print (",", end='')
    print(aflj_json[line]['cost'], end='')
    print (",", end='')
    print(aflj_json[line]['nlocals'], end='')
    print (",", end='')
    print(aflj_json[line]['offset'], end='')
    print (",", end='')
    print(aflj_json[line]['ebbs'], end='')
    print (",", end='')
    print(aflj_json[line]['nbbs'], end='')
    print (",", end='')
    print(aflj_json[line]['type'], end='')
    print (",", end='')
    print(aflj_json[line]['size'], end='')
    if 'datarefs' in aflj_json[line].keys():
        print (",", end='')
        print(len(aflj_json[line]['datarefs']), end='')
    if 'callrefs' in aflj_json[line].keys():
        print (",", end='')
        if len(aflj_json[line]['callrefs'])== 0:
            print(''',''')
        else:
            J_count = 0
            C_count = 0
            for elt in range(len(aflj_json[line]['callrefs'])): 
                if aflj_json[line]['callrefs'][elt]['type'] == "C":
                    C_count+=1
                if aflj_json[line]['callrefs'][elt]['type'] == "J":
                    J_count+=1
            print (C_count, end='')
            print(",", end='')
            print (J_count)
    else:
        print('')