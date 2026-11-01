class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:

        res = math.inf

        for i in range(0, len(nums), 2):
            one, two = nums[i], nums[i+1]
            res = min(int(str(one) + str(two)), res)

        return res
