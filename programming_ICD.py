# This program removes names and email addresses occurring in a given input file
# saves it in an output file.

import re
def deidentify():
    infilename = input("Give the input file name: ")
    outfilename = input("Give the output file name: ")

    infile = open(infilename,"r")
    text = infile.read()
    infile.close()

    # replace names
    nameRE = "(Ms\.|Mr\.|Dr\.|Prof\.) [A-Z](\.|[a-z]+) [A-Z][a-z]+|(?:Jr.|II|III|MS.|MBA.|DBA.|PhD.)"
    cnameRE = re.compile(nameRE)
    deidentified_text1 = re.sub(cnameRE, "**name**", text)


    # replace email addresses
    emailRE = "(\w+)@(\w+\.)+(edu|com|org|de|net)"
    cemailRE = re.compile(emailRE)
    deidentified_text = re.sub(cemailRE, "**email**", deidentified_text1)




# complete this

    outfile = open(outfilename,"w")
    print(deidentified_text, file=outfile)
    outfile.close()

deidentify()