class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:

        """
        my dumbass keeps defaulting to moving FORWARDS instead of BACKWARDS (i MUSt find the first occur of true instead of last)

        102 ms runtime beats 98%
        """
        
        def condition(k):
            return True if sum([ceil(num/k) for num in nums]) <= threshold else False
        
        l, r = 1, max(nums)

        while l < r:
            m = l + (r-l)//2

            if condition(m):
                r = m
            else:
                l = m+1

        return l
