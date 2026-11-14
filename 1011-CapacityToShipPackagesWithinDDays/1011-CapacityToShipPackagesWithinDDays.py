class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        """
        okay it was quite smooth but my dumbass initialized count at 0 instead of 1.

        oh also noticed my silly mistake of moving the wrong pointesr the wrong way before the submission told me im stupid asf so that was a good sign

        177 ms runtime beats 94%
        """
        
        def condition(cap):
            # note that it must be loaded in order or else itd be hell on earth (backtracking + binary search)
            count = 1
            curr = 0
            for weight in weights:  # make sure cap can at least handle any weights (max(weights))
                curr += weight
                if curr > cap:
                    curr = weight
                    count += 1
            return True if count <= days else False

        l, r = max(weights), sum(weights)

        while l < r:
            m = l + (r - l) // 2

            if condition(m):
                r = m
            else:
                l = m+1

        return l

        

        
