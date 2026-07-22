# You are given two sorted arrays.
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# Here:
    # nums1 has extra space (0s at the end) to hold all elements.
    # The first m elements (1,2,3) are valid.
    # nums2 has n valid elements.
# After merging, nums1 should become:
# [1,2,2,3,5,6]


def merge(nums1,m,nums2,n):
    i=m-1
    j=n-1
    k=m+n-1

    while i>=0 and j >=0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -=1
        else:
            nums1[k] = nums2[j]
            j -=1
        k -=1
    while j>=0:
        nums1[k] = nums2[j]
        j -=1
        k -=1
    return nums1

num1=[1,2,3,0,0,0]
num2 = [2,5,6]
print(merge(num1,len(num1)-len(num2),num2,len(num2)))
    


