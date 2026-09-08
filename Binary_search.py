def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1

arr = [10, 20, 30, 40, 50, 60]
target = 40

result = binary_search(arr, target)

print("Found at index:", result)

# using recursion

def binary_searchrec(arr, low, high, target):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return binary_searchrec(arr, mid + 1, high, target)

    else:
        return binary_searchrec(arr, low, mid - 1, target)


arr = [10, 20, 30, 40, 50]
target = 40

result = binary_searchrec(arr, 0, len(arr) - 1, target)

print("Found at index:", result)