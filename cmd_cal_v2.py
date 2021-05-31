#Comment
'''
Author: Bamidele Efunnuga
Desctiption: Command Line Based Calculator with users input
Creation Date: 31-05-2021
Version: 2.0
using functions
'''

print("Welcome to a Command Line Based Calculator.\n")

def caclulate(firstNum, secondNum, userOperator):
    
        # Calculation
        answer = 0
        if(userOperator == "x"):
            answer = firstNumber * secondNumber
        elif(userOperator == "+"):
            answer = firstNumber + secondNumber
        elif(userOperator == "-"):
            answer = firstNumber - secondNumber
        elif(userOperator == "/"):
            answer = firstNumber / secondNumber
        else:
            print("Operator defined unknown! please try again")

        return "The calculation of %s %s %s is equal to %s \n\n" %(firstNumber, userOperator, secondNumber, answer)

while True:
    try:
        # First Number User input that converts to a float
        firstNumber = float(input("Enter the first number in the calculation and press Enter: "))

        # Second Number User input that converts to a float
        secondNumber = float(input("Enter the second number in the calculation and press Enter: "))
        # Operator User input that converts to a float
        userOperator = input("Enter the operator of choice [ Add => +  | Subtract => -  | Divide => /  | Multiply => x | and press Enter: ")

        
        if(type(firstNumber) and type(secondNumber) == float):
            print(caclulate(firstNumber, secondNumber, userOperator))
          
    
    except ValueError:
        print("Your input is not a number! please check the input and try again.")
