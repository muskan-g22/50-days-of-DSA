# Given an integer array nums, move all 0s to the end while maintaining the relative order of non-zero elements.
def movezerolast(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            
            nums[fast] , nums[slow]=nums[slow],nums[fast]
            slow +=1
    return nums

def movezerofirst(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] == 0:
            
            nums[fast] , nums[slow]=nums[slow],nums[fast]
            slow +=1
    return nums

num = list(map(int , input("enter number separted by spaces: ").split()))
print(movezerolast(num))
print(movezerofirst(num))