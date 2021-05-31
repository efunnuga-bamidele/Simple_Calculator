#Comment
'''
Author: Bamidele Efunnuga
Desctiption: Command Line Based Calculator with users input
Creation Date: 31-05-2021
Version: 1.0
'''

print("Welcome to a Command Line Based Calculator.\n")
while True:
    # First Number User input that converts to a float
    firstNumber = float(input("Enter the first number in the calculation and press Enter: "))
    # Second Number User input that converts to a float
    secondNumber = float(input("Enter the second number in the calculation and press Enter: "))
    # Operator User input that converts to a float
    userOperator = input("Enter the operator of choice [ Add => +  | Subtract => -  | Divide => /  | Multiply => x | and press Enter: ")

    answer = 0
    # Calculation
    if(userOperator == "x"):
        answer = firstNumber * secondNumber
    elif(userOperator == "+"):
        answer = firstNumber + secondNumber
    elif(userOperator == "-"):
        answer = firstNumber + secondNumber
    elif(userOperator == "/"):
        answer = firstNumber / secondNumber
    else:
        print("Operator defined unknown! please try again")

    print("The calculation of %s %s %s is equal to %s \n\n" %(firstNumber, userOperator, secondNumber, answer))