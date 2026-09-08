class Solution:
    def hammingWeight(self, n: int) -> int:

        """
        this is a cheese, dont do this on interviews, will do bitwise ops vers next
        """
        
        s = bin(n)
        ctr = 0

        for char in s:
            ctr += 1 if char == "1" else 0

        return ctr
