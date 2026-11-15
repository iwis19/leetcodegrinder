class Solution:
    def countConsistent(self, nums: list[int]) -> int:

        """
        read constraints and it was 100 so brute is perfectly fine
        """

        n = len(nums)
        res = 0

        for i in range(n):
            running_and = mini = nums[i]
            res += 1
            for j in range(i+1, n):
                running_and &= nums[j]
                mini = min(mini, nums[j])

                if running_and == mini:
                    res += 1

        return res
        
