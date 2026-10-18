class Solution:
    def minDeletions(self, nums: list[int]) -> int:

        """
        idk why i used 2 ptr for this

        BUT GOOD FOR ME FOR REALIZING THE COMMENT THX DOUGGIE

        1 ms runtime beats 72%
        """

        deletions = 0

        # note that xor is only 0 on the exact same numbers.
        
        n = len(nums)
        unique = 0
        i = 1

        while i < n:
            if nums[i] == nums[unique]:
                deletions += 1
            else:
                unique = i
            i += 1

        return deletions
            
            
