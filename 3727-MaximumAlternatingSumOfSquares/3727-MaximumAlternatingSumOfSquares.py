class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        """
        with length n, split into half -> get sum

        easier than medium 

        219 ms runtime beats 39% but optimized so prolly need to work on a sol without subtract / add arrs
        """
        
        res = 0
        n = len(nums)

        nums = [ abs(nums[i])**2 for i in range(n) ]
        nums.sort()

        # if even, then n//2 add, n//2 subtract
        # if odd, then n//2+1 add, n//2 subtract

        # same case
        subtract = nums[:n//2]
        add = nums[n//2:]

        return sum( [add[i] for i in range(len(add))] ) - sum( [subtract[i] for i in range(len(subtract))] )

        


