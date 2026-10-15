class Solution:
    def sumCounts(self, nums: List[int]) -> int:

        """
        genuinely bugging
        """
        
        res = 0
        n = len(nums)

        for i in range(n):
            distinct_set = set()
            for j in range(i, n):
                distinct_set.add(nums[j])
                res += len(distinct_set) ** 2

        return res
