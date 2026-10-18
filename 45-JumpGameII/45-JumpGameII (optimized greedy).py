class Solution:
    def jump(self, nums: list[int]) -> int:
        
        """
        looked at solutions for a more optimized solution, this only scans everything once.

        we find the max reach jump within the specified range, then we just fully move on to the next unscanned area,
        without repeating scans like my original solution

        we can safely skip reiterating thru the older ones since they dont offer as much value anyways WHATSOEVER.

        3 ms runtime beats 90%
        """

        n = len(nums)

        if n == 1:
            return 0

        res = 0
        near = far = 0

        while far < n-1:
            
            farthest = 0

            for i in range(near, far+1): # include far
                farthest = max(farthest, i+nums[i])

            near = far+1
            far = farthest
            res += 1

        return res

