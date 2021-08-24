#To write acronym in output file
#acronym for each line in inputfile to same line in output file
def main():
    infile=input("Enter the input filename:")
    outfile=input("Enter the output filename:")
    file_ip = open("infile.txt", "r")
    file_op = open("outfile.txt","w")
    while True:
        line = file_ip.readline()
        words = line.split()
        acro = ""
        for w in words:
            acro = acro + w[0]
        acro = acro.upper()
        file_op.write(acro+"\n")
        if not line:
            break
    file_ip.close()
    file_op.close()


main()
