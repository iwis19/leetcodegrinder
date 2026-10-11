class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

        """
        quick bs daily
        """
        
        res = 0

        n = len(nums)

        for i, num in enumerate(nums):
            if not n % (i+1):
                res += num ** 2

        return res
