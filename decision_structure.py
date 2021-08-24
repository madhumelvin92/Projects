"""
The body mass index (BMI) is calculated as a person's weight (in pounds)
times 720, divided by the square of the person's height (in inches). A BMI
in the range 19-25, inclusive, is considered healthy. Write a program that
calculates a person's BMI and prints a message telling whether they are
above, within, or below the healthy range
"""


def calculateBMI(weight, height, outfile):
    bmi = (weight * 720) / (height ** 2)
    print('BMI is', bmi)
    if 19 <= bmi <= 25:
        message = "BMI is " + str(bmi) + "\nperson is healthy and within the healthy range"
    elif bmi < 19:
        message = "BMI is " + str(bmi) + "\nperson is below the healthy range"
    elif bmi > 25:
        message = "BMI is " + str(bmi) + "\nperson is above the healthy range"
    outputfile = open(outfile, 'w')
    outputfile.write(message)


def main():
    infile = input("enter the input file name: ")
    outfile = input("enter the output file name: ")
    inputfile = open(infile, 'r')
    values = []
    for i in inputfile:
        values.append(i)
    weight = int(values[0].strip('\n'))
    height = int(values[1])
    calculateBMI(weight, height, outfile)


main()
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
