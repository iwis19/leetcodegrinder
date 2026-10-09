class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        """
        this works because this way i dont have to consider n > 0 and n < 0. what im still wondering is that what if everything is just 0? since im starting min_prod and max_prod at 1 

        this is solved during the iteration process when n*prev_min/maxes and max / min is retrieved
        """
        
        min_prod = max_prod = 1
        res = max(nums)

        for n in nums:

            temp = min_prod
            min_prod = min(n * min_prod, n * max_prod, n)
            max_prod = max(n * temp, n * max_prod, n)

            res = max(res, max_prod)

        return res



