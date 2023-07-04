# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."

def factorial(number):
    if number < 0:
        return None
    elif number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

# Example usage
input_number = 5
factorial_result = factorial(input_number)

if factorial_result is None:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", input_number, "is", factorial_result, ".")
