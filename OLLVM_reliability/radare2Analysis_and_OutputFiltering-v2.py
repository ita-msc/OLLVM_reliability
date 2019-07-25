#!/usr/bin/python3
import sys
import r2pipe
import json


ANALYSIS_CMD        = "aa"
LISTING_CMD         = "aflj~{}"     # doesn't work with another non json formatted command for the moment



"""
    Radare2 analysis
"""
# opening the input executable file
r2 = r2pipe.open(str(sys.argv[1])) 


# basic analysis and listing the functions commands
r2.cmd(ANALYSIS_CMD)
radare2_output = r2.cmd(LISTING_CMD)


# loading the json output
radare2_output_json           = json.loads(radare2_output) 
radare2_output_lines_number   = len(radare2_output_json)




"""
    Radare2 output filtering
    The purpose of this protocol is to remove the least useful and relevant functions from the program and thus save the best of them.
    A "filtering formula" is applied to each function. Those with a score of 0 are automatically expelled from the sample of 
    individuals who will be involved in setting the final score.

    filtering_formula = (realsize + nbbs + realsize/nbbs) * number_of_jumps
"""
radare2_ready_to_be_scored = []

# applying the "filtering formula" to score each function of the program
for line in radare2_output_json:
    fcn_score = 0
    if not 'callrefs' in line.keys() or not line['callrefs']:
        fcn_score = 0
        line['filtering_score'] = fcn_score
    else:
        J_count = sum(cref['type']=="J" for cref in line['callrefs'])
        fcn_score = (line['nbbs'] + line['realsz'] + (line['realsz']/line['nbbs'])) * J_count
        line['filtering_score'] = fcn_score


# building the "ready-to-be-scored" list where each element has "filtering_score" > 0
for line in radare2_output_json:
    if line['filtering_score'] > 0.0 : 
        radare2_ready_to_be_scored.append(line)

print (radare2_ready_to_be_scored)