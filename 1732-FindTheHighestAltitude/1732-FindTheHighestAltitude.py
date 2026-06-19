class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        """
        used prefix sum, lowkey wasnt gonna, and also missed that u start at 0 ermmmmm

        0 ms runtime beats 100%
        """
        
        res = 0

        for i in range(len(gain)):
            
            temp = gain[i]
            
            if i > 0:
                gain[i] += gain[i-1]

            if gain[i] > res:
                res = gain[i]

        return res

