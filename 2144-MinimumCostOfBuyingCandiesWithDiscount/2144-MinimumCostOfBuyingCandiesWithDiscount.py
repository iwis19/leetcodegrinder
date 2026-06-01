class Solution:
    def minimumCost(self, cost: List[int]) -> int:

        """
        wow this is kinda stupid but i get it and i realized it too so its okay

        0 ms runtime beats 100%
        """
        
        descending = sorted(cost, reverse=True)

        n = len(descending)
        k = n//3
        res = 0

        for i in range(k):

            res = res + descending[i*3] + descending[i*3 + 1]

        if 3*k < n:

            for i in range(3*k, n):
                res += descending[i]

        return res
