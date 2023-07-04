# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."

# Create a list of numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Add a number
numbers.append(20)

# Remove a number
numbers.remove(3)

# Sort the list
numbers.sort()

# Print the updated list
print(numbers)


# When you run this program, it will output:

[1, 2, 4, 5, 6, 7, 8, 9, 10, 20]
