def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator(operator, x, y):
    while True:
        if operator == 'add':
            return add(x, y)
        elif operator == 'subtract':
            return subtract(x, y)
        elif operator == 'multiply':
            return multiply(x, y)
        elif operator == 'divide':
            return divide(x, y)
        else:
            return "Invalid operator"

        choiceforloop = input("Choose")
        if choiceforloop == "no":
            break
# Example usage:
operator = input("Enter operation (add, subtract, multiply, divide): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = calculator(operator, num1, num2)
print(result)