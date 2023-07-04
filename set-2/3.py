### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

# Input :

# s1 = "Ault"
# s2 = "Kelly"

# Expected Output:

# AuKellylt

s1 = "Ault"
s2 = "Kelly"

mid_index = len(s1) // 2
s3 = s1[:mid_index] + s2 + s1[mid_index:]

print(s3)
