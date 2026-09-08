class Solution:
    def countBits(self, n: int) -> List[int]:

        """
        this is an O(n) solution.

        it is dp where you store results from previous computes and reuse

        since we are shifting right and throwing out digits, we will always obtain smaller values. since n is sequentially monotonically increasing, we have already computed this and stored it in res. what we simply have to do is just compare the last bit, then reuse the previous results by throwing out hte rightmost compared bit.

        woo hoo, will come back
        """

        res = [0] * (n+1)
        for i in range(n+1):
            res[i] = (i & 1) + res[i >> 1]    

        return res
