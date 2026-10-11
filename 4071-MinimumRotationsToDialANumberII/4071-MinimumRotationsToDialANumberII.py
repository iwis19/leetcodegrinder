class Solution:
    def minRotations(self, n: int, s: str) -> int:

        """
        notice that dist(A, B) = dist(B, A) since dist(X,Y) = min(10 - |X-Y|, |X-Y|). under abs value, |X-Y| = |Y-X|

        therefore, the sum of dist of the suffix reversal is the same as non reversal

        let last num of 1st part be A, let first num of 2nd part be B, let last num of 2nd part be C
        obj is to find the corr loc to place the divider s.t. we obtain the maximum of:

        dist(A,B) - dist(A,C)

        needed some help on this by jipiti...

        1387 ms runtime beats 49%
        """

        def dist(curr, goal):
            return min(10 - abs(curr - goal), abs(curr - goal))

        if n == 1:
            return dist(0, int(s))

        max_saved_steps = 0
        
        # it would be: dig_0, dig_1, dig_2, ... dig_i-2, dig_i-1 |||| dig_i, dig_i+1, ... dig_n
        for i in range(n-1):
            b, c = int(s[i]), int(s[-1])

            #case where i = 0
            if i == 0:
                a = 0
            else:
                a = int(s[i-1])
            
            diff = dist(a, b) - dist(a, c)
            max_saved_steps = max(max_saved_steps, diff)

        res = 0
        curr = 0
        for i in range(n):
            res += dist(int(curr), int(s[i]))
            curr = s[i]

        return res - max_saved_steps

        
