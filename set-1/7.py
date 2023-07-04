# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

# Example usage
input_number = 13
if is_prime(input_number):
    print(input_number, "is a prime number.")
else:
    print(input_number, "is not a prime number.")


# 13 is a prime number.
