class Solution:
    def reverseBits(self, n: int) -> int:
        
        """
        thought process:
        - compare to the other end of n?
        
        final ans: extract while shifting left ?

        bitwise ops will take some tiem for me to digest since it alternates between a decimal format with a binary format and is easy to get lost in.

        we are creating a new result. we read the final bit of n, then add this bit to the result, and then shift n to the right so i can retrieve another digit.
        """

        res = 0

        for _ in range(32):
            bit = n & 1
            res <<= 1
            res |= bit

            n >>= 1

        return res


