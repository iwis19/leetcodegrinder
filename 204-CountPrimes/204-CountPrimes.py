class Solution:
    def countPrimes(self, n: int) -> int:

        """
        haha did this from the leetcode contest td will try to retain this

        2040ms runtime beats 85%
        """

        if n < 2:
            return 0
        
        # strictly less than n
        is_prime = [True] * n

        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return len([ i for i in range(n) if is_prime[i] ])
