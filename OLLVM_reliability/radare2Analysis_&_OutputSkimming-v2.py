#!/usr/bin/python3
import sys
import r2pipe
import json


################################################## USER SECTION #######################################################
# Choose the analysis and listing commands you want to apply to the input file (NO REAL NEED TO CHANGE THESE)
ANALYSIS_CMD        = "aa"
LISTING_CMD         = "aflj~{}"     # doesn't work with another non json formatted command for the moment

#######################################################################################################################


"""
    Radare2 analysis
"""
# opening the input executable file
r2 = r2pipe.open(str(sys.argv[1])) 



# basic analysis and listing the functions commands
r2.cmd(ANALYSIS_CMD)
radare2_output = r2.cmd(LISTING_CMD)



# loading and processing the json output
# loading json output
radare2_output_json           = json.loads(radare2_output.decode("utf-8")) 
radare2_output_lines_number   = len(radare2_output_json)


"""
    Radare2 output skimming
    [explain here the output skimming protocol]
"""
radare2_ready_to_be_scored = 
for line in radare2_output_json:
    print ()