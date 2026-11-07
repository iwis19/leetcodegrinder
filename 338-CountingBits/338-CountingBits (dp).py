class Solution:
    def countBits(self, n: int) -> list[int]:

        """
        very smart dp approach tbh:

        i>>i always guarantees a smaller value (therefore already precomputed) since i>>1 = floor(i/2).

        removing the LSB is valid since were also js adding back the LSB if it exists, we could also do MSB if we wanted to
        """
        
        ans = [0] * (n+1)

        for i in range(n+1):
            ans[i] = ans[i >> 1] + (i&1)

        return ans
