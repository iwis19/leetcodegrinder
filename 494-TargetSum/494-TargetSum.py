class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        """
        2 am beast mode, need a hint on memoization though because top down memoization is still a bit confusing

        how to tell i need a memoization:
        - will results likely be reused? -> yes here
        - how many cases compared?
            plain dfs: 2^n = 2^20 which caused TLE
            memoization dfs: say max sum (all positive signs) for nums = S. then -S <= sum <= S w/ alternating signs
            we also run up to i = n runs, so 20*(2S+1) is way smaller than 2^20 
        - there are many cases where cached results arent even used, but this isnt one

        218 ms runtime beats 11%. some people did some cool math things to do bottom up dp construction / tabulation
        to get the 20 ms runtime.
        """
        
        memo = {}

        def dfs(i, curr_sum):

            if i == len(nums):
                return 1 if curr_sum == target else 0

            if (i, curr_sum) in memo: # dip early bc its in memo i can just reuse it
                return memo[(i, curr_sum)]

            add, sub = curr_sum + nums[i], curr_sum - nums[i]

            add = dfs(i+1, curr_sum + nums[i])
            sub = dfs(i+1, curr_sum - nums[i])

            memo[(i, curr_sum)] = (add + sub)

            return memo[(i, curr_sum)]

        return dfs(0,0)
