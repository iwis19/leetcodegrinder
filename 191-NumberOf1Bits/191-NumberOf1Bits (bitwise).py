class Solution:
    def hammingWeight(self, n: int) -> int:

        """
        very clever thing about bitwise ops:
        - python displays normal base 10, but the system uses binary already
        - hence i dont need to explicitly convert to binary using bin()
        - i can straight up do my bitwise ops on the decimal number i see and itll still work!
        """
        
        ctr = 0

        while n:
            if n & 1: ctr += 1
            n >>= 1

        return ctr

