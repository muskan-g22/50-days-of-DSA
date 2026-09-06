# Given an integer array nums and an integer k, return the k most frequent elements.

# heap sort complexity O(n log k)
import heapq

def topKFrequents(nums, k):

    frequency = {}

    # Count frequency
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    heap = []

    # Keep only k elements in heap
    for num, freq in frequency.items():

        heapq.heappush(heap, (freq, num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]

# more better Bucket sort - O(n)

def topKFrequent(nums, k):

    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in frequency.items():
        buckets[freq].append(num)

    result = []

    for freq in range(len(buckets) - 1, 0, -1):

        for num in buckets[freq]:

            result.append(num)

            if len(result) == k:
                return result

list = [1,1,1,2,3,3,2,3]
print(topKFrequents(list,2))
print(topKFrequent(list,2))