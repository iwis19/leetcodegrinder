class Solution:
    def countCommas(self, n: int) -> int:
        
        """
        0->999: no comma
        1000->100000: 1 comma
        """

        res = 0

        if n < 1000:
            return 0

        return n - 1000 + 1
