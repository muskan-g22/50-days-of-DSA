# Given an integer array nums, return an array answer such that:
# answer[i] = product of every element in nums except nums[i]

def productExceptSelf(nums):

    n = len(nums)

    answer = [1] * n

    # Calculate prefix products
    prefix = 1

    for i in range(n):

        answer[i] = prefix

        prefix *= nums[i]

    # Calculate suffix products
    suffix = 1

    for i in range(n - 1, -1, -1):

        answer[i] *= suffix

        suffix *= nums[i]

    return answer


# Driver Code

nums = list(map(int, input("Enter array elements: ").split()))

result = productExceptSelf(nums)

print("Product except self:", result)