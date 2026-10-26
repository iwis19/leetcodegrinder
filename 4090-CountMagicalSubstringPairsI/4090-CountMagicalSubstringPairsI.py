class Solution:
    def countMagicalPairs(self, s: str) -> int:

        """
        fix i and j, check all remaining k
        move j, check all remaining k
        move i, loop again
        """

        ans = 0
        n = len(s)

        for j in range(n-1):
            distinct1, distinct2 = {}, {}
            seen1, seen2 = set(), set()

            for i in range(j, -1, -1):
                seen1.add(s[i])
                if len(seen1) not in distinct1:
                    distinct1[len(seen1)] = 0
                distinct1[len(seen1)] += 1

            for k in range(j+1, n):
                seen2.add(s[k])
                if len(seen2) not in distinct2:
                    distinct2[len(seen2)] = 0
                distinct2[len(seen2)] += 1

            for key, val in distinct1.items():
                if key in distinct2:
                    ans += distinct1[key] * distinct2[key]

        return ans
