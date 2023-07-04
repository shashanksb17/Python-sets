# 3. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"

def two_sum(nums, target):
    # Create a dictionary to store the complement of each number
    complements = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in complements:
            return [complements[complement], i]
        complements[num] = i

    return None

# Main program
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print(result)
