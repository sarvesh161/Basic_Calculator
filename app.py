# This is a basic calulator.

# A function for addition
def addition(num1, num2):
    return num1 + num2

# A function for subtraction
def subtraction(num1 , num2):
    return num1 - num2

# A function for multiplication
def multiplication(num1 , num2):
    return num1 * num2

# A function for division
def division(num1 , num2):
    return num1 / num2

# A function to take input from user
def input():
    print('Choose the operation:\n')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    input = int(input('Enter your choice: '))
    return input