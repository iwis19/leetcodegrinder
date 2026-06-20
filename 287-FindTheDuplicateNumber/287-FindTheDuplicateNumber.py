class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        """
        pretty simple problem but it was more about optimizing, wanted to see if htere is a better approach but it was simply to exit when you find out frequency exceeds 1 during increment

        11 ms runtime beats 99%
        """
        
        n = len(nums)  # true length of the actual arr, n = 5, then max num is 4, and freq contains 0 1 2 3 4
        freq = [0] * n

        for num in nums:

            freq[num] += 1
            if freq[num] > 1:
                return num
            
        return
