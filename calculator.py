# Program to build a simple calculator

def calculator():
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))

    print("Press 1 for Addition, 2 for Subtraction, 3 for Multiplication or 4 for Division")
    choice = int(input("Enter your choice: "))

    # for addition
    if choice==1:
        print("The sum of the numbers is:", a+b)
        print()

    # for subtraction
    elif choice==2:
        print("The difference of the numbers is:",a-b)
        print()

    # for multiplication
    elif choice==3:
        print("The product of the numbers is:",a*b)
        print()
    
    # for division
    elif choice==4:
        if b!=0:
            print("The quotient of the numbers is:",a/b)
            print()
        else:
            print("Invalid Division!!")
            print()

    # if the user enters a choice other than the digits 1,2,3 or 4
    else:
        print("Invalid Operator!!")
        print()

    calculator()

calculator()
