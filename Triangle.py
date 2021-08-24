# This program calculates the area of a triangle.
import math


def main():
    print("This program calculates the area of a triangle.")
    a = float(input("Side a:"))
    b = float(input("Side b:"))
    c = float(input("Side c:"))
    s = (a + b + c) / 2
    print("Value of S : ", s)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Area of the triangle is:", area)

main()






