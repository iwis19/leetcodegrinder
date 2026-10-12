class Solution:

    """
    NEED to remember maxPrimes solution, very useful. hopefully i retain this.

    weekly contest problem no runtime info
    """
    
    def maxPrimes(self, n: int, s: int) -> list[int]:

        if s < 2:
            return []

        def find_primes(n):

            is_prime = [True] * n
            is_prime[0] = is_prime[1] = False
            
            for i in range(2, int(n**0.5)+1):
                if is_prime[i]:
                    for j in range(i*i, n, i):
                        is_prime[j] = False

            return [ i for i in range(n) if is_prime[i] ]

        primes = find_primes(min(n,s)+1)
        n = len(primes)

        sum = 0
        res = []
        i = 0

        while i < n and sum+primes[i] <= s:
            prime = primes[i]
            sum += prime
            res.append(prime)
            i += 1

        return res
        
