#!/usr/bin/python3
import csv
import sys

"""
    input: scoringresults_[ollvm_version]_i.csv
    output: finalscores-[ollvm-version].csv

    This scripts gathers all obfuscated average scores and non-obfuscated average scores in an output file
    the csv file will be formatted this way:
    Obfuscated scores, Non obfuscated scores
"""


csv_reader = csv.reader(open(str(sys.argv[1]),mode='r'), delimiter=',')

next(csv_reader)    # don't take the first lin into account
for row in csv_reader:
    if "./" not in row[0]:  #   the name of a program starts with, we only want to gather the average scores 
        if "Non obfuscated" not in row[0]:  # if name of the first column refers to an obfuscated score
            print(str(row[1]), end="")
        else:
            print(","+ str(row[1]))

    