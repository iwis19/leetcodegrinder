class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:

        """
        dp problem? if the previous elements work, and this current element also works,
        then all prev combos would work

        turned out to be prefix sum
        """

        n = len(nums)
        cond = [ False ] * n

        for i in range(n):
            if minK <= nums[i] <= maxK: 
                cond[i] = True

        tot = 0
        
        for i in range(n):
            if cond[i]:
                if i-1 < 0 or not cond[i-1]:
                    nums[i] = 1
                else:
                    nums[i] = 1+nums[i-1]
                tot += nums[i]

        return tot
