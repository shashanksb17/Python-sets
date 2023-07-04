# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"

def fibonacci_sequence(n):
    sequence = []

    if n >= 1:
        sequence.append(0)
    if n >= 2:
        sequence.append(1)

    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)

    return sequence

# Example usage
input_n = 5
fibonacci_result = fibonacci_sequence(input_n)
print(fibonacci_result)
