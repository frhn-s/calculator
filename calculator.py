def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def divide(x, y):
    if y == 0:
        return 'Cannot divide by zero!'
    else:
        return x / y
    
def multiply(x, y):
    return x * y

number1 = float(input('Enter the first number: '))
number2 = float(input('Enter the second number: '))
operations = input('Enter the operation (+, -, *, /)')

if operations == '+':
    result = add(number1, number2)
elif operations == '-':
    result = minus(number1, number2)
elif operations == '/':
    result = divide(number1, number2)
elif operations == '*':
    result = multiply(number1, number2)

print('Answer: ', result)