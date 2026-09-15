
# You are given two arrays nums1 and nums2.

# For every element in nums1, find the next greater element of that element in nums2.

# The next greater element means the first element to the right that is greater than the current element.

# If no greater element exists, return -1.

def nextGreaterElement(nums1, nums2):

    stack = []
    next_greater = {}

    for num in nums2:

        while stack and num > stack[-1]:
            smaller = stack.pop()
            next_greater[smaller] = num

        stack.append(num)

    return [next_greater.get(num, -1) for num in nums1]


# =========================
# Driver Code
# =========================

nums1 = list(map(int, input("Enter nums1: ").split()))
nums2 = list(map(int, input("Enter nums2: ").split()))

result = nextGreaterElement(nums1, nums2)

print("Next Greater Elements:", result)