# Given a sorted array, remove the duplicates in-place.
# Return the number of unique elements.
# The first k elements of the array should contain all unique values.

def removeduplicate(nums):
    if len(nums)==0:
        return 0
    slow = 0
    for fast in range(1,len(nums)):
        if nums[fast] != nums[slow]:
            slow +=1
            nums[slow] = nums[fast]
    return slow+1

nums = [1,1,2]
print(removeduplicate(nums))