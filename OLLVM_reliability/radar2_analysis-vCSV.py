import sys
import r2pipe
import json
import os
from itertools import repeat
import math

# ------------------------------------------------------------------------------------------------------------------------------------
# This script intends to decide, thanks to the output data it generates, which sorting criterion to use in the radar2_analysis-v2.py 
# ------------------------------------------------------------------------------------------------------------------------------------

################################################## USER SECTION #######################################################
# Choose the analysis and listing commands you want to apply to the input file
ANALYSIS_CMD        = "aa"
LISTING_CMD         = "aflj~{}"
PERCENTAGE          = 0.3
SORTING_CRITERION   = "nbbs"        # size, nbbs, ratio
#######################################################################################################################



# opening the input executable file
print("Opening the input executable file")
r2 = r2pipe.open(str(sys.argv[1])) 



# basic analysis and listing commands
r2.cmd(ANALYSIS_CMD)
aflj_output = r2.cmd(LISTING_CMD)



# loading and processing the json output
print("Loading and processing the json output...")
aflj_json           = json.loads(aflj_output)
aflj_lines_number   = len(aflj_json)
complete_aflj_data_array = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] for i in repeat(None, aflj_lines_number)]



"""
    STEP 1 => Building complete_aflj_data_array array
    :structure: array of arrays:
                [
                    [offset_0, nbbs_0, size_0],
                    [offset_1, nbbs_1, size_1],
                    ...
                    [offset_n, nbbs_n, size_n]
                ]
    :size: n = number of output lines of the aflj r2 command
"""
for line in range(aflj_lines_number):
    complete_aflj_data_array[line][0]=aflj_json[line]['name']
    complete_aflj_data_array[line][1]=aflj_json[line]['offset']
    complete_aflj_data_array[line][2] = aflj_json[line]['nbbs']
    complete_aflj_data_array[line][3] = aflj_json[line]['size']
    complete_aflj_data_array[line][4]=aflj_json[line]['calltype']
    complete_aflj_data_array[line][5]=aflj_json[line]['realsz']
    complete_aflj_data_array[line][6]=aflj_json[line]['diff']
    complete_aflj_data_array[line][7]=aflj_json[line]['cc']
    complete_aflj_data_array[line][8]=aflj_json[line]['indegree']
    complete_aflj_data_array[line][9]=aflj_json[line]['args']
    complete_aflj_data_array[line][10]=aflj_json[line]['difftype']
    complete_aflj_data_array[line][11]=aflj_json[line]['edges']
    complete_aflj_data_array[line][12]=aflj_json[line]['outdegree']
    complete_aflj_data_array[line][13]=aflj_json[line]['cost']
    complete_aflj_data_array[line][14]=aflj_json[line]['nlocals']
    complete_aflj_data_array[line][15]=aflj_json[line]['ebbs']
    complete_aflj_data_array[line][16]=aflj_json[line]['type']
  