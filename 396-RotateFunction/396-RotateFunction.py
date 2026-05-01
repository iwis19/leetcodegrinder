class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        """
        i feel like the tag honestly is a pretty misleading thing sometimes, it said dp, but i solved it using prefix sum (keep adding and working on things as i go thru iteratively)

        im going to start noting down techniques and idk if they count as dsa liek the algo part but im going to make a separate page on notion

        anyways i had to peek the sol to see if i really needed dp but turns out i didnt so i figured out the algo myself (most of it)

        O(n) optimized
        """
        
        n = len(nums)
        res = -math.inf
        total = sum(nums)

        val = sum([i*nums[i] for i in range(n)])

        # n orientations
        for i in range(n):

            """
            going from f(0) -> f(1)

            add all values in nums besides n-1
            subtract (n-1)*nums[n-1]


            going from f(k) -> f(k+1)

            add all values in nums besides n-k-1
            subtract (n-1)*nums[n-k-1]
            """

            # val = val + total - nums[n-i-1] - (n-1)*nums[n-i-1]
            # val = val + total - n*nums[n-i-1]
            val = val + total - n*nums[n-i-1]
            res = max(res, val)

        return res

           R
