# square_calculator.py

def square(number):
    return number * 3

# Get user input
user_input = float(input("Enter a number to square: "))
result = square(user_input)

# Display the result
print(f"The square of {user_input} is {result}.")