class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        """
        apparently this is kadanes algorithm? not too sure how this is dp either

        but i really understand the intuition now:
        - if curr_sum is negative, why would i keep it? since anything minus a number is EVEN smaller.
        - if curr_sum is positive, then ill keep adding to it and see whats up

        28 ms runtime beats 80%
        """
        
        res = sum(nums)

        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = num
            else:
                curr_sum += num

            res = max(res, curr_sum)

        return res
        
