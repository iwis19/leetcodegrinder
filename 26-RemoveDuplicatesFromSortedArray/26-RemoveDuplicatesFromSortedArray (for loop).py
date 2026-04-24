class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        """
        kinda disappointed with this one idk

        1. i knew i had to use two pointer, one to keep track of unique numbers, another one to keep on swapping
        2. i first set up a while loop and 2 vars, which was honestly correct, but my code was off since i checked j with j-1 instead of i-1, def gonna try the thing i was doing earlier out now

        0 ms runtime beats 100
        """

        n = len(nums)

        i = 1

        for j in range(1, n):

            if nums[j] == nums[i-1]:
                continue
            else:
                nums[i] = nums[j]
                i += 1

        return i

            

