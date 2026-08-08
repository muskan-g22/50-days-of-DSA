# Given an array of positive integers nums and a positive integer target, 
# find the minimum length of a contiguous subarray whose sum is greater than or equal to target.

def minsubarray(nums,target):
    left , current_sum = 0,0
    min_length = float("inf")
    for right in range(len(nums)):
        current_sum = nums[right]
        while current_sum >=target:
            min_length = min ( right-left+1, min_length)
            current_sum -= nums[left]
            left +=1
    if min_length == float("inf"):
        return 0
    return min_length

nums = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target: "))

answer = minsubarray(nums,target)

print("Minimum subarray length:", answer)