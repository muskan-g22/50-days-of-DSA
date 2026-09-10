# Given an integer array nums and an integer k, return the kth largest element in the array.

import heapq

def klargestnumber(nums,k):
    heap = []
    for num in nums:
        heapq.heappush(heap,num)
        if len(heap)>k:
            heapq.heappop(heap)
    return heap[0]

nums=list(map(int,input("Enter array: ").split()))
k = int(input("Enter k: "))


print("Kth largest element:", klargestnumber(nums,k))