import sys
import r2pipe
import json
import os
from itertools import repeat
import math

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
shorted_aflj = [[0,0,0] for i in repeat(None, aflj_lines_number)]



"""
    STEP 1 => Building shorted_aflj array
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
    shorted_aflj[line][0]=aflj_json[line]['offset']
    shorted_aflj[line][1] = aflj_json[line]['nbbs']
    shorted_aflj[line][2] = aflj_json[line]['size']



"""
    STEP 2  => Descending sorting according to the SORTING_CRITERION chosen by the user (see USER SECTION) 
"""
sorted_aflj_by_sorting_criterion    = []

if (SORTING_CRITERION == "nbbs"):
    sorted_aflj_by_sorting_criterion = sorted(shorted_aflj, key= lambda shorted_aflj: shorted_aflj[1], reverse=True)
    chosen_outputs_number = int(math.ceil(PERCENTAGE * len(sorted_aflj_by_sorting_criterion)))
if (SORTING_CRITERION == "size"):
    sorted_aflj_by_sorting_criterion = sorted(shorted_aflj, key= lambda shorted_aflj: shorted_aflj[2], reverse=True)
    chosen_outputs_number = int(math.ceil(PERCENTAGE * len(sorted_aflj_by_sorting_criterion)))
if (SORTING_CRITERION == "ratio"):
    sorted_aflj_by_sorting_criterion = sorted(shorted_aflj,key= lambda shorted_aflj: shorted_aflj[2]/shorted_aflj[1], reverse=True)
    chosen_outputs_number = int(math.ceil(PERCENTAGE * len(sorted_aflj_by_sorting_criterion)))



"""
    STEP 3  => Shortening sorted_aflj_nbbs array: PERCENTAGE chosen by the user (see USER SECTION)
            => Extracting offsets from chosen_outputs array and converting them into hexadecimal format
"""
chosen_outputs  = []
offsets         = []

for output in range(chosen_outputs_number): 
    chosen_outputs.append(sorted_aflj_by_sorting_criterion[output])
    offsets.append(hex(chosen_outputs[output][0]))



# generating .dot files in a corresponding directory
print("Generating the following .dot files...")
directory_name  = sys.argv[1] + ".dir"
mkdir_cmd       = "mkdir " + directory_name
os.system (mkdir_cmd)

for offset in range(chosen_outputs_number):
    dot_file_generation_cmd = "ag "+str(offsets[offset])+" > ./"+str(sys.argv[1]) + ".dir"+"/"+str(sys.argv[1])+str(offset+1)+".dot"
    print (dot_file_generation_cmd)
    r2.cmd(dot_file_generation_cmd)

final_message = "\nAll done! A '/"+ str(sys.argv[1]) + ".dir' directory has just been created in this folder. Check this out! :)"
print(final_message)
print("Use 'xdot [dot_file]' command to view the generated .dot files.")
