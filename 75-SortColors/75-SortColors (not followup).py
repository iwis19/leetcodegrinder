class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        initially thought of quicksort esp with the 2ptr, but later saw that theres only 0,1,2 so did counting sort

        0 ms ru ntime beats 100%, but bad space complex
        """
        
        zeroes, ones, twos = 0, 0, 0

        for num in nums:
            if num == 0:
                zeroes += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1

        for i in range(len(nums)):
            # when i is smaller than zeroes, put in all 0s
            if i < zeroes:
                nums[i] = 0
                continue

            # when i is smaller than zeroes + ones - 1, put in all 1s
            if i < zeroes + ones:
                nums[i] = 1
                continue

            # when i is smaller than zeroes + ones + twos - 1, put in all 2s
            if i < zeroes + ones + twos:
                nums[i] = 2
                continue
