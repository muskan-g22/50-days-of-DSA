# Given an integer array nums, return:
# True if any value appears at least twice
# False if every element is unique

def duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

num1 = [1,2,3,1]
print(duplicate(num1))
num2 = [1,2,3]
print(duplicate(num2))