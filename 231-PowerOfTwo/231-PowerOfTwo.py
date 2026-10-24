class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False
        
        one_bits = 0

        """
        since python doesnt really define ints or whatever with set amount of bytes, it can go up to even 1k bits
        so unlike cpp where i can do set 32 loops, i do while n > 0

        0 ms runtime beats 100% for dwharder
        """
        i = 0

        while n > 0:

            if n & 1:
                if one_bits:
                    return False
                one_bits += 1

            n >>= 1

        return True
