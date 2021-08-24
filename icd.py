# A function that makes a dictionary from ICD codes;
# codes as keys and disease name as values
import re

def ICD_dictionary():
    d = {}

    infile = open("icdo3.txt", "r")
    for line in infile:  # regular expression to read the codes and dieseas names
        r = re.search("(\d+/\d+)\s+(.+)", line)
        if (r):
            code = r.group(1)
            code = code.replace("/", "")
            disease = r.group(2)
            disease = disease.rstrip()

            disease = disease.lower()
            d[code] = disease
    infile.close()
    return d

