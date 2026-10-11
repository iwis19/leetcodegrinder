class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        """
        pos dividend, neg divisor - add divisor until 0
        pos dividend, pos divisor - subtract divisor until 0
        neg divident, pos divisor - add divisor until 0
        neg divident, neg divisor - subtract divisor until 0

        but should notice that abs(7/3) == abs(7/-3) == abs(-7/-3) == abs(-7/3)
        """

        res = 0

        if not dividend:
            return res

        while abs(dividend) >= abs(divisor):
            
            if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
                dividend += divisor
                res -=1
            elif (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
                dividend -= divisor 
                res += 1

        return res

        
