class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:

        """
        dummy sol
        """

        if 9*num < sum:
            return ""

        res = []
        i = 0

        while sum > 0 and i < num:
            subtract = min(9, sum)
            res.append(str(subtract))
            i += 1
            sum -= subtract

        for j in range(num-i):
            res.append("0")

        return "".join(res)
