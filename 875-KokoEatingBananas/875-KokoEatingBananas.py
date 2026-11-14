class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        """
        binary search???

        a very good generalized template:

        1. define lower and upper bounds that i want to be checking out in a problem
        2. define a condition for a number to pass
        3. determine monotonicity

        remember that binary search is always about something monotonic. if koko can eat bananas in m hours here,
        then it can eat in m+1 hours as well, and beyond. 

        "find the first true in a sequence of false, false, false, ... true, true ..."

        this is acctually so cool i didnt know binary search was this goated before lol good to know ill be back

        162 ms runtime beats 82%
        """

        def condition(k):
            hours = sum([ ((pile-1) // k + 1) for pile in piles ])  # check for amount of total hours that i need
            return True if hours <= h else False

        l, r = 1, max(piles) # because koko can only eat one pile at once anyways

        while l < r:
            m = l + (r - l) // 2  # praccy for dougie cuz this is safer in cpp

            # since were finding first occurrence, then if this fits, we can move right to m to search earlier, but not
            # throw this one away since we cant (might be the 1st one alr)
            if condition(m):
                r = m
            else:
                l = m+1

        return l

