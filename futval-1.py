# A program to compute the value of an investment
# carried in the number of years into the future

def main() :
    print("This program computes the value of an investment in the given number of years.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter the no of investment years : "))

    principal = principal * (1 + apr)**year

    print ("The value in"+ str(year)+"years is: ",principal)

main()    

