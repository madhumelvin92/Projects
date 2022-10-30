"""
The program reads the contents of this file into a dictionary, closes the file and presents user with the following menu
choices in an infinite loop:

Add an entry
Show value for a key
Delete an entry
Save the file
Print the current dictionary
Quit
Complete rest of the program to process the dictionary interactively with the user. The following appropriate actions should be taken for each one of them and then the menu should be shown again unless the user quits.
Add an entry: Ask the user for the key and value, and make an entry, if the key already exists then prompt the user whether to overwrite its value.
Show value for a key: Ask the user for the key and show the corresponding value, point out if the key does not exist.
Delete an entry: Ask the user for the key and delete the entry, point out if the key does not exist
Save the file: Save to the same file name in the same comma-separated format (do not worry about the order of entries), make sure to close the file
Print the current dictionary:  show value entries of the current dictionary on the screen (in alphabetical order of the keys).
End the program. If the dictionary has been modified since the last save, then prompt the user whether it should be saved before quitting.
"""


# An incomplete program for an "infinite" interactive loop to process a dictionary.

def main():
    d = {} # dictionary

    # Read the file's contents in the dictionary d
    filename = input("Give the file name: ")
    file = open(filename,"r")
    for line in file:
        # read key and value
        key, value = line.split(",")
        # remove whitespaces before and after
        key = key.lstrip()
        key = key.rstrip()
        value = value.lstrip()
        value = value.rstrip()
        # insert entry in the dictionary
        d[key] = value
    file.close()



    loop=True # continue looping if true


    while (loop):
        print("\n\nEnter one of the following menu choices:")
        print("1 Add an entry")
        print("2 Show value for a key")
        print("3 Delete an entry")
        print("4 Save the file")
        print("5 Print the current dictionary")
        print("6 Quit")
        choice = input("Choice 1-6: ")
        print("\n\n")

        if (choice=="1"): # Add an entry
            k = input("Give the key: ")
            v = input("Give its value: ")
            # complete the rest
            if k in d:
                ow = input("Key already exist, overwrite value:(y/n)? ")
                # Ask for whether user wants to overwrtie if key already exists.
                if (ow == 'y'):
                    d[k] = v
                else:
                    pass
            else:
                d[k] = v
        elif (choice=="2"): # Show value for a key
            k = input("Give the key: ")
            # complete the rest
            if d.get(k) == None:
                print("Key does not exist.")
            else:
                print("The Value is : " + d.get(k))
        elif (choice=="3"): # Delete an entry
            k = input("Give the key to delete the entry: ")
            # complete the rest
            if k in d:
              del d[k]
              print("Updated Dictionary :",d)
            else:
                print("Key does not exist.")
        elif (choice=="4"): # Save the file
             print("Saving the file")
             # complete the rest
             file=open("example.txt", 'w')
             for k, v in d.items():
                 key = str(k)
                 value = str(v)
                 file.write(key + ', ' + value + '\n')
             file.close()
        elif (choice=="5"): # Print the current dictionary
             # complete the rest
            for key in sorted(d):
                print('key:',key +', value:',d[key])
        elif (choice=="6"): # Quit
            # complete the rest
            choice = input('Do you want to Save the file before Quitting? Y/N?')
            if choice == 'Y' or choice == 'y':
                print("Saving the file")
                file = open("example.txt", 'w')
                for k, v in d.items():
                    key = str(k)
                    value = str(v)
                    file.write(key + ', ' + value + '\n')
                file.close()
                loop = False
            else:
                loop = False
        else :
            print("Incorrect choice")

main()
