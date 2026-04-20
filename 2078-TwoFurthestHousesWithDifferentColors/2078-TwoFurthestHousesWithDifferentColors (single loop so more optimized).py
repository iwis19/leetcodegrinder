class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        """
        singular loop
        
        0 ms runtime beats 100
        """
        
        res = 0

        for i in range(len(colors)):
            if colors[i] != colors[0]: res = max(res, i)
            if colors[i] != colors[-1]: res = max(res, len(colors)-i-1)

        return res
