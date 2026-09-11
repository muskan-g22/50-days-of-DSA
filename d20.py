# Problem

# You are given an n × n matrix where:

# Every row is sorted in ascending order.
# Every column is sorted in ascending order.

# Find the kth smallest element.


import heapq

def kthSmallest(matrix, k):
    heap = []

    n = len(matrix)

    # Add first element of every row
    for row in range(n):
        heapq.heappush(heap, (matrix[row][0], row, 0))

    # Remove smallest k times
    for _ in range(k):
        value, row, col = heapq.heappop(heap)

        # Add next element from the same row
        if col + 1 < n:
            heapq.heappush(
                heap,
                (matrix[row][col + 1], row, col + 1)
            )

    return value


n = int(input("Enter matrix size: "))

matrix = []

print("Enter matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

k = int(input("Enter k: "))

answer = kthSmallest(matrix, k)

print("Kth smallest element:", answer)