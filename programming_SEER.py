"""
Using SEER dataset attached below find the total number of occurrences of various breast cancers
separately for men and women in four age groups (0-24; 25-49; 50-74; 75+) .
Save the output in a .csv file with nine things per line separated by commas:
the cancer type (remove commas from this), total number of occurrences in men aged 0-24,
and total number of occurrences in women aged 0-24, and so on.  Use names from ICD-O3 for cancer types.
You may print only the cancer types whose codes are found in ICD-O3 and it need not be
in any particular order.  Submit your .py file in Canvas.

Character positions in SEER file:
Sex  24
Age at diagnosis  25-27
Year of birth  28-31
Histology Type ICD-O-3  53-56
Behavior Code ICD-O-3  57

"""
import icd
import os


def main():

    infile = open("SEER_Breast_cancer.txt",'r')
    dirs = os.listdir()


    men24_di = {}
    women24_di = {}
    men49_di = {}
    women49_di = {}
    men74_di = {}
    women74_di = {}
    above75men_di = {}
    above75women_di = {}


    for line in infile:
        disease = line[52:57]
        gender = line[23]
        age = int(line[24:27])
        men = (gender == "1")
        women = (gender == "2")
        if men:
            if (age <= 24):
                men24_di[disease] = men24_di.get(disease, 0) + 1
            elif (25 <= age <= 49):
                men49_di[disease] = men49_di.get(disease, 0) + 1
            elif (50 <= age <= 74):
                men74_di[disease] = men74_di.get(disease, 0) + 1
            elif (age >= 75):
                above75men_di[disease] = above75men_di.get(disease, 0) + 1
        elif women:
            if (age <= 24):
                women24_di[disease] = women24_di.get(disease, 0) + 1
            elif (25 <= age <= 49):
                women49_di[disease] = women49_di.get(disease, 0) + 1
            elif (50 <= age <= 74):
                women74_di[disease] = women74_di.get(disease, 0) + 1
            elif (age >= 75):
                above75women_di[disease] = above75women_di.get(disease, 0) + 1
    infile.close()

    icdo_di = icd.ICD_dictionary()  # use the ICD-O dictionary to get the names for the codes
    #print(icdo_di)
    outfile = open("output.csv", "w")
    print("Cancer Type", ",", 'Men 0-24', ",", 'Women 0-24', ",", 'Men 25-49', ",", 'Women 25-49', ",", 'Men 50-74', ",",
          'Women 50-74', ",", 'Men>=75', ",", 'Women>=75', file=outfile)
    #print(women24_di)
    #print(men24_di)
    for code in icdo_di:
        #print(code)
        #print(women24_di)
        W24 = women24_di.get(code, 0)  # 0-24 age women that get this cancer
        M24 = men24_di.get(code, 0)  # 0-24 age men that get this cancer
        W49 = women49_di.get(code, 0)  # 25- 49 age women that get this cancer
        M49 = men49_di.get(code, 0)  # 25 -49 age men that get this cancer
        W74 = women74_di.get(code, 0)  # 50-74 age  women that get this cancer
        M74 = men74_di.get(code, 0)  # 50-74 age men that get this cancer
        Above75W = above75women_di.get(code, 0)  # greater than 75 age women that get this cancer
        Above75M = above75men_di.get(code, 0)  # greater than 75 age men that get this cancer
        print(icdo_di[code].replace(",", ""), ",", M24, ",", W24, ",", M49, ",", W49, ",", M74, ",", W74, ",", Above75M,
              ",", Above75W, file=outfile)
    outfile.close()

    print("output.csv outfile")


main()

