class Solution:
    def minMoves2(self, nums: list[int]) -> int:

        """
        i was originally thinking of a sum array, and then i check based on each element im on
        i assume im moving all to that and i edit 

        and then i thought about using averages or modes since i had a hard time reasoning about using medians

        i suppose it is the right idea because:
        1. averages only work in linear distribution
        2. in skewed distribution, median shows "central tendency"
        3. mean is not usually the middle of the distribution 

        its like exam mark distributions

        3 ms runtime beats 83%
        """

        nums.sort()
        mid = len(nums)//2

        if len(nums)%2:
            median = nums[mid]
        else:
            median = (nums[mid-1] + nums[mid]) // 2

        return sum([ abs(num - median) for num in nums ])

        
