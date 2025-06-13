# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)  # Convert numerator to float and num stands for numerator
        den = float(denominator)  # Convert denominator to float and den stands for denominator

        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."