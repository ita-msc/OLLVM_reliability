#!/usr/bin/python3
import sys 
import csv

# Scores initialization:
obfuscated_score = 0.0
non_obfuscated_score = 0.0



csv_reader = csv.reader(open(str(sys.argv[1]),mode='r'), delimiter=',')
next(csv_reader)
for row in csv_reader:
    if "fla" in row[0] or "sub" in row[0] or "bcf" in row[0] or "strobf" in row[0]:   # if the name of the program contains anything related to obfuscation
        obfuscated_score+=float(row[1])
    else:       # if the name of the program tells that the program is not obfuscated
        non_obfuscated_score+=float(row[1])


# Calculate the average score for the obfuscated et non obfuscated programs:
size = len(list(csv.reader(open(str(sys.argv[1])))))-1  # total of both the obfuscated and non obfuscated programs (minus 1, to exclude the name of the columns' row
obfuscated_score = obfuscated_score/(size/2)
non_obfuscated_score = non_obfuscated_score/(size/2)


# Write these two scores at the end of the csv formatted scoring results file:
csv_writer = csv.writer(open(str(sys.argv[1]),mode='a'), delimiter=',')
csv_writer.writerow(["Obfuscated final score", str(obfuscated_score)])
csv_writer.writerow(["Non obfuscated final score", str(non_obfuscated_score)])
