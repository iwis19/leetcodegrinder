class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        """
        <= checks for whether or not an exacct candidate exists -> finding where a number / outcome is
        < checks for closest / a boundary -> finding the location to insert smth
        """
        
        l, r = 1, num

        while l <= r:
            m = l + (r-l)//2
            sqr = m*m

            if sqr == num:
                return True
            if sqr < num:
                l = m+1
            else:
                r = m-1

        return False
