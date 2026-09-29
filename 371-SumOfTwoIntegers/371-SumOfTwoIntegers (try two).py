class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0b11111111111111111111111111111111
        max_int_and_1 = 2**31

        # keep adding the two bits last bits of 2 ints

        """
        sum (without carry) = a^b
        carry = a&b << 1

        set a, b = sum, carry

        and i keep going until there is no b

        010
        011

        this is the second time ive done this problem and last time they did NOT have negative numbers in these test cases 

        lowkey also didnt remember 1 shotting sum and carry and repeating, only thought about adding 1 by 1 and stuff 

        ALSO got a good refresher that in positive ints (32 bit), leading bit is always 0. 

        0111 is 7
        1000 is -8
        1111 is -1

        so we need to apply bitmasks (bit 1 for 32 bits) onto the number everytime we do an operation to keep the numbers within the int size after operations on negative numbers as well

        since there are no minus signs in this program, instead of a <= max_int were using a < max_int_and_1. for negative results, we apply bitmask and then do ~x.

        ~x = -x - 1.

        e.g. 111101 masked by 111111 = 000010, this means 2. then ~2 gives -2-1 = -3
        """

        while b:

            add = (a^b) & mask # preserves binary digits but establioshes 32 bits
            carry = (a&b) & mask  # same as above
            a, b = add, carry << 1

        return a if a < max_int_and_1 else ~(a ^ mask)
        

        
        
