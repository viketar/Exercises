def add():
    z = float(input("Please enter a number: "))
    y = float(input("Enter another number: "))
    print(z + y)

def substraction():
    z = float(input("Please enter a number: "))
    y = float(input("Enter another number: "))
    print(z - y)

def multiply():
    a = float(input("Knappa in ett nr: "))
    b = float(input("Ett till nr, tack: "))
    print(a * b)

def divide():
    a = float(input("Ange ett nr: "))
    b = float(input("Ange ett till nr: "))
    print(a / b)

operation = input("Please type +, -, * or /: ")
if operation == '+':
    add()
elif operation == '-':
    substraction()
elif operation == '*':
    multiply()
elif operation == '/':
    divide()
