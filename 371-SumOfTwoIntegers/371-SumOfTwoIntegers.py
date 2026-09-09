class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        """
        original thought process:

        a =  10
        b =  11
        -------
        c = 101

        all bitwise ops:

        &  AND
        ^  XOR
        |  OR
        ~  NOT

        >> right shift
        << left shift

        since this is addition, the amt of bits in the binary representation matters... (TURNED OUT TO BE FALSE)
        probably make them the same abt of bits, then add? idk through what though (ALSO FALSE)

        CAME UP WITH THIS: 
        i think rule is that when both are 1, i get 0 -> sounds like XOR, but i also need to push an extra 1 to the bit forward

        100% need to come back to this.
        """

        # get the sums (without carry overs) with ^ -> since 0,0 gives 0 and 1,1 gives 0 as well, while preserving 1 and 0s.
        # get the carry overs with & since only under & would a 1,1 stay as a 1.

        # missing piece: keep a var for the carry overs, then keep adding carry overs to the XOR results until carry overs dont exist anymore.

        carry, sum_no_carry = (a & b) << 1, a ^ b    # MUST REMEMBER: << and >> ARE PRIORITIZED, SO DONT FORGET TO PLEASE PUT BRACKETS

        while carry:
            new_carry = (carry & sum_no_carry) << 1
            new_sum_no_carry = carry ^ sum_no_carry
            carry, sum_no_carry = new_carry, new_sum_no_carry

        return sum_no_carry

