class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        
        """
        seems like a dp problem because what we choose early on decides what we can step on later

        backwards tabulation?

        n = 4, costs = [ 5 1 6 2 ], then ans = 
        
        [ 5 1 6 2 ]
        [ 5 1 9 2 ]
        [ 5 7 9 2 ]
        [ 13 7 9 2 ]

        bruh i had the right idea all along but i didnt know its 1-indexed and im starting at 0

        so technically im starting at -1 geeg

        had the right idea n everything tho good for me

        379ms runtime beats 57%
        """

        for i in range(n-2, -2, -1):
            one = two = three = math.inf

            if i+1 < n: one = costs[i+1] + 1
            if i+2 < n: two = costs[i+2] + 4
            if i+3 < n: three = costs[i+3] + 9
            
            res = min(one, two, three)
            if i == -1:
                return res

            costs[i] += res
        
        return 0
