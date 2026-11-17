class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:

        """
        nothing wrong with impl i was genuinely bugged out of my mind because i denoted mid as m and i was like why it no work

        and somehow double runtime than other LITERALLY EXACT SAME IMPLS. optimized my thing asw before it was like 800 ms

        487 ms runtime ebats 17%
        """

        n = len(bloomDay)

        if m*k > n:
            return -1
        
        def condition(day):
            # they must be adjacent. we can just go in order + see if we can grab k in a row
            bouqs = 0
            count = 0

            for i in range(n):
                if bloomDay[i] <= day:
                    count += 1
                    if count == k:
                        bouqs += 1
                        count = 0
                else:
                    count = 0

            return bouqs >= m

        l, r = min(bloomDay), max(bloomDay)

        while l < r:
            mid = l + (r-l) // 2

            if condition(mid):
                r = mid
            else:
                l = mid+1

        return l


            
