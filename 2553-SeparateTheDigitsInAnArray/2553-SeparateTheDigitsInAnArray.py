class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        """
        all logics and optimization right

        0 ms beats 100%
        """
        
        res = []

        for num in nums:

            s = str(num)
            for i in range(len(s)):
                res.append(int(s[i]))

        return res
