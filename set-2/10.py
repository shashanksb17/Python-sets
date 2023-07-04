### Problem **10: Modify the tuple**

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

# **Given**:

# ```
# tuple1 = (11, [22, 33], 44, 55)
# ```

# **Expected output:**

# tuple1: (11, [222, 33], 44, 55)

tuple1 = (11, [22, 33], 44, 55)

modified_tuple = tuple(tuple1)  # Convert the original tuple to a mutable list
modified_tuple[1][0] = 222  # Modify the first item of the list

modified_tuple = tuple(modified_tuple)  # Convert the modified list back to a tuple

print("tuple1:", modified_tuple)
