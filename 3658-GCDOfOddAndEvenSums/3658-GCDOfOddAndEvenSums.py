class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:

        """
        okay im so rusty i did not remmeber how to use this gcds algo, but tbh i used it once/ twice before. so its fine. i hop ei remember

        used O(n) instead of O(1) -> there is n^2 and n^(n+1) for even and odd, withouit having to loop through all n
        """
        
        a,b = n**2, n*(n+1)

        # euclidean algorithm: keep dividing with the remainder -> a = b * q + r, and set a = b, b = r, and repeat until r hits 0

        r = 1
        while r != 0:
            r = a % b 
            if not r:
                return b
            a, b = b, r

        return None
