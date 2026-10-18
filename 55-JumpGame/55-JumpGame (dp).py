class Solution:
    def canJump(self, nums: list[int]) -> bool:
        
        """
        its must max step count at nums[i], not that it has to jump exactly that many steps

        i needed help on this with the dp solution, never in a million years would i think to go backwards

        18 ms runtime beats 65%, bottom up tabulation dp
        """

        n = len(nums)
        reachable = [False] * n
        reachable[n-1] = True
        last_reachable_i = n-1

        for i in range(n-2, -1, -1):
            if i+nums[i] >= last_reachable_i:
                reachable[i] = True
                last_reachable_i = i
        
        return reachable[0]
