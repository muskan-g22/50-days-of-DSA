# Problem

# You are given a list of points on a 2D plane:

# points = [[1,3],[-2,2],[5,8],[0,1]]
# k = 2

# Find the k points closest to the origin (0,0).

# Example

# For:

# points = [[1,3],[-2,2],[5,8],[0,1]]
# k = 2

# Distance from origin:

# [1,3]  → 1² + 3² = 10
# [-2,2] → (-2)² + 2² = 8
# [5,8]  → 25 + 64 = 89
# [0,1]  → 0² + 1² = 1

# The 2 closest points are:

# [0,1]
# [-2,2]
import heapq
def kclose(points,k):
    heap = []
    for x,y in points:
        distance = x*x + y*y
        heapq.heappush(heap,(-distance,x,y))
        if len(heap)>k:
            heapq.heappop(heap)
    result=[]
    for distance,x,y in heap:
        result.append([x,y])
    return result

points =[]
n = int(input("Enter no. of points : "))
for i in range(n):
    x,y = map(int,input(f"Enter points {i+1}: ").split())
    points.append([x,y])
k = int(input("Enter k : "))
print(" k closest point : ", kclose(points,k))
