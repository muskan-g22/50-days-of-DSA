def counting_sort(arr):

    max_value = max(arr)
    count = [0] * (max_value + 1)

    for num in arr:
        count[num] += 1

    result = []

    for num in range(len(count)):
        result.extend([num] * count[num])

    return result


arr = [4, 2, 2, 8, 3, 3, 1]

print(counting_sort(arr))