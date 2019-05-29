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

columnTitleRow = "programName,calltype, realsz, diff, name, cc, indegree, nargs, difftype, edges, outdegree, cost, nlocals, offset, ebbs, nbbs, type, size, datarefs, cref_c, cref_j\n"
parameters = ["calltype", "realsz", "diff", "name", "cc", "indegree", "nargs", "difftype", "edges", "outdegree", "nlocals", "cost", "offset", "ebbs", "nbbs", "type", "size"]

for output in aflj_json:
    row1 = str(sys.argv[1]) + ","
    row2 = ""
    for element in output:
        J_count = 0
        C_count = 0
        if (element in parameters):
        # just print it properly
            row1+= str(output[element]) + ","
        else:
            if (element == "callrefs"):
            # count the number of J and C
                if (len(output[element]) == 0): # if there is no callref
                    row2+= "N\A,N\A,"
                else: # if there is at least one callref
                    for cref in range(0, len(output[element])):
                    # for each {type: type_value, addr: addr_value, at: at_value}
                        if ((output[element][cref]['type']) == 'J'):
                            J_count+=1
                        else: 
                            C_count+=1
                    row2+= str(C_count) + "," + str(J_count) + ","
            if (element == "datarefs"):
            # count the number of elements in the datarefs list
                if (len(output[element]) == 0): # if there is no dataref
                    row2+= "nodataref,"
                else:
                    row2+=str(len(output[element])) + ","
    print (columnTitleRow)
    print (row1 + row2)