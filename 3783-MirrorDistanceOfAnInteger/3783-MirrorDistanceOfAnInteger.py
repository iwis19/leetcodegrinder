class Solution:
    def mirrorDistance(self, n: int) -> int:

        """
        amazing!!!!

        0 ms runtime beats 100
        """
        
        def reverse(num):
            
            # e.g. 1240
            res = 0
            while num > 0:

                digit = num % 10   # retrieves the last digit: 0, 4, 2, 1
                res = res * 10 + digit  # multiplies prev results: 0, 4, 42, 421
                num //= 10 # takes out last digit: 124, 12, 1, 0
            
            return res

        return abs(n - reverse(n))
