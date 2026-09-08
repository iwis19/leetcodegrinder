class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def bits(n: int) -> int:
            ctr = 0
            while n:
                ctr += n & 1
                n >>= 1
            return ctr

        res = [0] * (n+1)
        for i in range(n+1):
            res[i] = bits(i)

        return res
