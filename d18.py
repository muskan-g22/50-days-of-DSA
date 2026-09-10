# Given an integer array nums and an integer k, find the kth smallest element.

import heapq

def ksmallnumber(nums,k):
    heap = []
    for num in nums:
        heapq.heappush(heap,-num)
        if len(heap)>k:
            heapq.heappop(heap)
    return -heap[0]

nums=list(map(int,input("Enter array: ").split()))
k = int(input("Enter k: "))


print("Kth smallest element:", ksmallnumber(nums,k))