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
    A SCORING_FORMULA is applied to each function. Those with a score of 0 are automatically expelled from the sample of 
    individuals who will be involved in setting the final score.

    The SCORING_FORMULA is used both for the filtering and the scoring phases.
"""
radare2_filtered = []
radare2_ready_to_be_scored = []
the_unwanted_ones = ["sym.__libc_csu_fini", "sym._dl_relocate_static_pie", "entry0", "entry1.init", "sym.imp.__libc_start_main"]



# expelling unrelevant functions and applying the SCORING_FORMULA to score each remaining function of the program

for line in radare2_output_json:
    if not line['name'] in the_unwanted_ones:   # don't take into account the 'unwanted functions'
        if not 'callrefs' in line.keys() or not line['callrefs']:
            fcn_score = 0
            line['score'] = fcn_score
        else:
            J_count = sum(cref['type']=="J" for cref in line['callrefs'])   # calculate the number of jumps
            SCORING_FORMULA     = (line['realsz']/line['nbbs']) * J_count
            fcn_score = SCORING_FORMULA
            line['score'] = fcn_score
            radare2_filtered.append(line)   # add the line and its score to the filtered list
    


"""
    Scoring 
    The final score is calculated from a filtered sample.
    This condensed list normally contains only functions that are considered useful and relevant for the scoring phase
    Functions with a score of 0 are expelled because they do not have jumps.

    Warning:    The SCORING_FORMULA is likely to evolve, taking into account the scores obtained with different formulas that we have tried and which have not been conclusive due to the size of the sample being too small.
                So first thing you'll need to do, is increasing the number of programs you'll compile (10 turned out to be not enough!)
"""
# building the "ready-to-be-scored" list where each element has "score" > 0
for line in radare2_filtered:
    if line['score'] > 0.0 : 
        radare2_ready_to_be_scored.append(line)


for line in radare2_ready_to_be_scored:
    prgm_score = 0.0
    prgm_score+= line['score']
prgm_score = prgm_score/len(radare2_ready_to_be_scored) # calculate the average score for the input program



print (str(sys.argv[1]) +"," + str(prgm_score)) # csv formatted print

