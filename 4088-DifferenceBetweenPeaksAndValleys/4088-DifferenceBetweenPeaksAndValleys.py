class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:

        """
        during contest
        """

        peak_sum = valley_sum = 0

        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                peak_sum += nums[i]
            elif nums[i-1] > nums[i] and nums[i+1] > nums[i]:
                valley_sum += nums[i]

        return peak_sum - valley_sum
