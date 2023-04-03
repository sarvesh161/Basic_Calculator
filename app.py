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

# Code to choose operartion
cont = True
while(cont):
    print('Choose the operation:\n')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    inpt = int(input('Enter your choice: '))

#Code to implement the operation
    if inpt not in [1 , 2 , 3 , 4]:
        print('Wrong input. Try again')
        continue
    else:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))

        if inpt == 1:
            print(addition(num1 , num2))
        elif inpt == 2:
            print(subtraction(num1 , num2))
        elif inpt == 3:
            print(multiplication(num1 , num2))
        else:
            print(division(num1 , num2))

# Code to try the process again
    cont2 = True
    while(cont2):    
        print('Do you want to continue?')
        choice = input('Enter your choice: ')

        if choice.upper() in ['Y' , 'YES']:
            cont = True
            cont2 = True
        elif choice.upper() in ['N' , 'NO']:
            cont = False 
            cont2 = False
        else:
            print('Answer as yes or no')
            continue