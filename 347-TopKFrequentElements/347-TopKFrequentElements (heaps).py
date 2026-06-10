import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        damn heaps are nice

        okay refresher since i had to search a LOT up

        6 ms runtime beats 56%
        """
        
        h = []

        freq = {}

        for num in nums:

            if num not in freq:
                freq[num] = -1
                continue
            freq[num] -= 1
        
        for num, count in freq.items():
            heapq.heappush(h, (count, num))

        res = []

        for i in range(k):
            res.append(heapq.heappop(h)[1])
        
        return res
