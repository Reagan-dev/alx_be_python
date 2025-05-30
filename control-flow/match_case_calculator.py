# simple calculator with match case
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# use match case to perform the operation
match operation:
    case '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}.")
    case '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}.")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please choose from +, -, *, or /.")
