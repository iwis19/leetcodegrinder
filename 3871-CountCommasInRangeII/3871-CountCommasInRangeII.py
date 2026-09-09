class Solution:
    def countCommas(self, n: int) -> int:
        
        """
        1,000,000,000,000,000

        0 - 999
        1,000 - 999,999
        1,000,000 - 999,999,999
        1,000,000,000 - 999,999,999,999
        1,000,000,000,000 - 999,999,999,999,999
        1,000,000,000,000,000

        highkey was bugging out and tapped out to doom scroll linkedin + instagram but locked in and fixed in 2 mins

        0ms runtime beats 100%
        """

        floors = [
            999,
            999_999,
            999_999_999,
            999_999_999_999,
            999_999_999_999_999,
            999_999_999_999_999_999
        ]
        l = len(floors)

        res = 0

        for i, floor in enumerate(floors):
            if n < floor:
                break
            if n > floor:
                res += (i+1) * (min(n, floors[i+1]) - floor)

        return res
