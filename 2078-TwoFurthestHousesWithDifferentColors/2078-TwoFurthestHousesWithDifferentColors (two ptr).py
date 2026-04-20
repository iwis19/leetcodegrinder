class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        """
        double two pointerrrr

        1. had a bit of small trouble working with indices like len(colors) - l - 1, other than that im optimal yay
        2. also maybe shouldve used a forloop tbh

        0 ms runtime beats 100
        """
        
        l, r = 0, len(colors)-1
        res = 0

        while r > 0:

            if colors[0] == colors[r]:
                r -= 1
                continue
            
            res = max(res, r)
            break

        while l < len(colors):

            if colors[l] == colors[len(colors)-1]:
                l += 1
                continue
            
            res = max(res, len(colors)-l-1)
            break

        return res
