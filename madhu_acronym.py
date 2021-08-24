# This program gives the acronyms of a phrase entered by user.
def main():
    print("This program gives the acronyms of a phrase entered by user.")
    phrase = input("Enter the phrase: ")
    word = phrase.split()
    acronym = ""
    # Loop for taking out first character of every word and change to upper case
    for firscharacter in word:
        acronym = acronym + firscharacter[0].upper()
    print("The acronym for your phrase is ", acronym + ".")


main()
