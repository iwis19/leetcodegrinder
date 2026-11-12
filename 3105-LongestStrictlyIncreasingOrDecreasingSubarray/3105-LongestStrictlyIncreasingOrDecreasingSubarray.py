class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        """
        quick daily

        1 ms runtime beats 80%
        """
        
        res = inc = dec = 1

        for i in range(1, len(nums)):
            
            #inc
            if nums[i] > nums[i-1]:
                inc += 1
                res = max(res, inc, dec)
                dec = 1

            #dec
            elif nums[i] < nums[i-1]:
                dec += 1
                res = max(res, inc, dec)
                inc = 1

            else:
                res = max(res, inc, dec)
                inc = dec = 1

        return res

            

            
