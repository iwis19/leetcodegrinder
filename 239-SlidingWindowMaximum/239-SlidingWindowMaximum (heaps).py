from heapq import heapify, heappush, heappop
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        """
        okay i learned a bit more about lazy deletion. only delete when needed.

        originally knew to use a heap and was thinking abt a deque or smth but idk i think thats not optimal,
        still really slow though. needed a hint on also storing the index along w nums[i] to see if its valid
        to be included or not

        bro the exemplar sol does use deque and its so nonchalant it just uses a deque to only
        keep track of valid maxes.
        it 1. purges invalid loc maxes, and 2. takes out more if curr q[-1] are smaller than curr q[i], and then
        appends i into the q at the end. and when i hits k-1, it starts appending to ans arr

        831 ms runtime beats 5% LMAO
        """
        
        heap = [ (-nums[i], i) for i in range(k) ]   # max heap rn
        heapify(heap)
        n = len(nums)
        ans = [ -heap[0][0] ]

        """
        few cases:

        curr_max is getting removed, need to take second max
        curr_max isnt getting removed, new element > curr_max
        curr_max isnt getting removed, nothing changes

        keep a monotonic stack of increments? like i implement the min stack idea

        i go from min -> max in that problem to max -> min here

        or i just use heaps?
        """

        for i in range(1, n-k+1):  # start from i, interval goes from i->i+k-1

            while heap and heap[0][1] < i:
                heappop(heap)

            print(i, i+k-1, n)
            heappush(heap, (-nums[i+k-1], i+k-1))

            ans.append(-heap[0][0])

        return ans
            
            

