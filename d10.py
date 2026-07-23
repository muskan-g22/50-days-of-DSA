# Suppose there are n versions of a product.
# Initially every version is good.
# Then one version becomes bad.
# Every version after that is also bad.
# Your task is to find the first bad version.

FIRST_BAD = 6


def isBadVersion(version):
    return version >= FIRST_BAD


def firstBadVersion(n):
    """
    Finds the first bad version using Binary Search.
    """
    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2

        if isBadVersion(mid):
            # Mid might be the first bad version
            right = mid
        else:
            # First bad version must be after mid
            left = mid + 1

    return left


n = int(input("Enter the total number of versions: "))

answer = firstBadVersion(n)

print("First Bad Version:", answer)