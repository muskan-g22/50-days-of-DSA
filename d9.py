# Binary search 
# Given a sorted array and a target value, return the index of the target.
# If the target is not found, return -1.

def binarysearch(nums,target):
    left = 0
    right = len(nums)-1
    while left <=right:
        mid = (left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return -1

nums=list(map(int,input("enter sorted array elements separted by space: ").split()))
n = int(input("enter element to be search: "))
print(binarysearch(nums,n))