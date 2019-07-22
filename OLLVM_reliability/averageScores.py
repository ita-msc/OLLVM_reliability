#!/usr/bin/python3
import sys 
import csv


"""
    input:  finalscores-[ollvm-version].csv
    output: finalscores-[ollvm-version].csv

    This script calculates the average score from the ones gathered in the input file and adds it at the end of this same file.
"""
obfuscated_average_score = 0.0
non_obfuscated_average_score = 0.0


csv_reader = csv.reader(open(str(sys.argv[1]),mode='r'), delimiter=',')
next(csv_reader)    # don't take into account the first line


for row in csv_reader:
    obfuscated_average_score+=float(row[0]) # row[0] gathers all obfuscated scores
    non_obfuscated_average_score+=float(row[1]) # row[1] gathers all non obfuscated scores



# Calculate the average score for the obfuscated et non obfuscated programs:
size = len(list(csv.reader(open(str(sys.argv[1])))))-1  # total of both the obfuscated and non obfuscated programs (minus 1, to exclude the name of the columns' row
obfuscated_average_score = obfuscated_average_score/size
non_obfuscated_average_score = non_obfuscated_average_score/size


# Write these two scores at the end of the csv formatted scoring results file:
csv_writer = csv.writer(open(str(sys.argv[1]),mode='a'), delimiter=',')
csv_writer.writerow(["Obfuscated average score", str(obfuscated_average_score)])
csv_writer.writerow(["Non obfuscated average score", str(non_obfuscated_average_score)])
