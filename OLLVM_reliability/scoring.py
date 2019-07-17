#!/usr/bin/python3
import sys 
import csv

csv_reader = csv.reader(open(str(sys.argv[1]),mode='r'), delimiter=',')
obfuscated_score = 0.0
non_obfuscated_score = 0.0
size = len(list(csv.reader(open(str(sys.argv[1])))))-1  # total of both the obfuscated and non obfuscated programs (minus 1, to exclude the name of the columns' row)
    
next(csv_reader)

for row in csv_reader:
    if "fla" in row[0] or "sub" in row[0] or "bcf" in row[0] or "strobf" in row[0]:   # if the name of the program contains anything related to obfuscation
        obfuscated_score+=float(row[1])
    else:       # if the name of the program tells that the program is not obfuscated
        non_obfuscated_score+=float(row[1])



print(obfuscated_score/(size/2))
print(non_obfuscated_score/(size/2))

csv_writer = csv.writer(open(str(sys.argv[1]),mode=''), delimiter=',')
csv_writer.writerow('coucou')
# csv.writer("\n\n"+ "Obfuscated final score,"+ str(obfuscated_score))
# csv_reader.write("Non obfuscated final score,"+ str(non_obfuscated_score))

