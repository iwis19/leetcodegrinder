class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:

        """
        dumbed out for like 2 minutes because i used a while loop instead of mod im so dumb

        3 ms runtime beats 78%
        """

        if 9*num < sum:
            return ""
        
        nine, last = sum // 9, sum % 9

        res = "9" * nine
        res += str(last) if last else ""

        i = 1 if last else 0

        res += "0" * (num-nine-i)

        return res
