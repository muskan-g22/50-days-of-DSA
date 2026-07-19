# Given an array of integers nums and an integer target, return the indices of the two numbers whose sum equals target.

def twosum0(nums, target):  # complexity is O(n^2)
    for i in range (len(nums)):
        for j in range (len(nums)):
            if nums[1]+nums[j]==target:
                return [i,j]


# optimal solution
# complexity is O(n)

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:    
            return [seen[complement], i]

        seen[num] = i

nums=[2,6,7,9,0]
print(twoSum(nums,9))