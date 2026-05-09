class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        initially had tle, but figured i used n^2 instead of 3n like rn, so its fixed now, will try constant extra space now!

        32 ms runtime beats 30%
        """
        
        # prefix and suffix

        n = len(nums)
        prefix, suffix, res = [1] * n, [1] * n, [0] * n

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(n):
            res[i] = prefix[i]*suffix[i]

        return res


        
