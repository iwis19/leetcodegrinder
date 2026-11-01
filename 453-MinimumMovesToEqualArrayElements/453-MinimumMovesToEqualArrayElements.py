class Solution:
    def minMoves(self, nums: list[int]) -> int:

        """
        cool daily... how was anyone supposed to think of incrementing n-1 by 1 means decrementing 1 by 1

        9 ms runtime beats 50%
        """
        
        goal = min(nums)
        ans = 0

        for num in nums:
            ans += num - goal

        return ans
