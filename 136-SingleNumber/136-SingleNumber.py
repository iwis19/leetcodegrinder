class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        """
        a first introduction to bitwise ops

        ^ is called XOR. rule is:
        - 0 ^ x = x
        - x ^ x = 0
        - 0 ^ 0 = 0

        can be shown in bit level operations as well.
        """
        
        n = len(nums)
        running_xor = 0

        for num in nums:
            running_xor ^= num

        return running_xor

