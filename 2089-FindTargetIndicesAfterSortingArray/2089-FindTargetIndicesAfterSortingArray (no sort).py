class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:

        """
        geeg sm better beats 99.5% of space complexity too lol
        """
    
        smaller = 0
        ctr = 0

        for num in nums:
            if num == target:
                ctr += 1
            elif num < target:
                smaller += 1

        return [ i+smaller for i in range(ctr) ]
