class Solution:
    def mySqrt(self, x: int) -> int:
        
        """
        part two of my binary search journey tonight

        continue same idea

        this one is different because i think its like true, true, ... , true, false, false ...
        and im trying to find the last true

        w solve + impl
        
        JUST learned that:
        when i do l=m, r=m-1, i need to ROUND UP in m -> (l+r+1)//2
        when i do l=m+1, r=m, i just keep it normal -> (l+r)//2

        3 ms runtime beats 76%
        """

        def condition(n):
            return n * n <= x

        l, r = 0, x

        """
        test 

        x = 8
        l,r,m = 0,8,4
        l,r,m = 0,3,1
        l,r,m = 1,3,2
        l,r,m = 2,3,2
        """

        while l < r:
            m = l + (r-l+1)//2

            if l == m:
                return m
            if condition(m):
                l = m
            else:
                r = m-1

        return l

