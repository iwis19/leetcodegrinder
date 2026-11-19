class Solution:
    def minimizeSum(self, nums: List[int]) -> int:

        """
        GENUINE cheeks problem
        """
        
        n = len(nums)
        if n <= 3:
            return 0

        """
        so after changing 2 nums, i want to find + minimize

        (max(nums) - min(nums)) + (two closest values)

        but i should def use the lowscore as an opportunity to either bring max value down, or bring min value up.
        """

        nums.sort()

        """
        1 4 5 7 8
        """
        return min([nums[n-1] - nums[2], nums[n-3] - nums[0], nums[n-2] - nums[1]])



