class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        """
        i m just not supposed to start editing from the back even though i thought i was supposed to be since i didnt have to clean up the order of the end either i hope i understand this soon
        """
      

        index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        
        return index
