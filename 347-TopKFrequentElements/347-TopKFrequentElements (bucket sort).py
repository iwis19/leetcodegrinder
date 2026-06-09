class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        bucket sort is the idea of putting items into groups based on some property, and then processing the buckets instead of just straight up 
        trying to process the given data

        in this problem, the property is frequency.

        will do more bucket sorting after, its not really like its OWN algorithm like actual sort algos, more of an idea

        will do heaps on this next

        15 ms runtime beats 9%
        """
        
        n = len(nums)

        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 1
                continue
            freq[num] += 1

        buckets = [ [] for i in range(n+1) ]  # because edgecase is all n numbers in nums are the same, so we need a bucket as big as n. (1 indexed.)

        for num, count in freq.items():
                buckets[count].append(num)  # the bucket stores 0 appearance, 1, 2, 3, all the way to n

        res = []
        i = n

        while k > 0:

            bucket = buckets[i]
            while k > 0 and bucket:
                res.append(bucket.pop(0))
                k -= 1

            i -= 1

        return res


