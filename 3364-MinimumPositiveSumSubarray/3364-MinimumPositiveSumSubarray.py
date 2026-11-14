class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        """
        bruteforce daily, need a lot of work on sliding windows

        65 ms beats 28%
        """
        
        res = math.inf
        n = len(nums)

        for i in range(n):
            running_total = 0
            for j in range(i, n):
                if j-i+1 > r:
                    break
                running_total += nums[j]
                if l<=j-i+1<=r and running_total > 0:
                    res = min(res, running_total)
                
        return -1 if res == math.inf else res
