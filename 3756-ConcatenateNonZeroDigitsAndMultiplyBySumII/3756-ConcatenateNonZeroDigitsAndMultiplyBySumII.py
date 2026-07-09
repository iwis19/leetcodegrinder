class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        """
        okay i swaer im booty i will get on this grind in a few days after blueprint 

        tech learned: 
        - without precomputating array pow, then the computes would be m*q instead of m+q in optimal tc. 
        - by precalculating, we replace calculating pow(10, a[r] - a[l], MOD) everytime manually but simply access it 
        
        doing all this pow[] arr and also prefix_count is for:
        - when i have 123456 and i want to remove 123, its not simply 123456-123, its rather 123456 - 123000

        4000+ ms beats 5%... but i think optimal tc idk whats going on though.
        """

        MOD = 1000000007
        MAX = 100001
        pow = [1] * MAX
        for i in range(1, MAX):
            pow[i] = (pow[i-1] * 10) % MOD

        n = len(s)
        res = []
          # sum of everything STRICTLY BEFORE this index
        prefix_digits = [0] * (n+1)  # digits of everything STRICTLY BEFORE this index

        prefix_sum, prefix_digits, prefix_count = [0] * (n+1), [0] * (n+1), [0] * (n+1)

        for i in range(n):
            number = int(s[i])
            prefix_sum[i + 1] = prefix_sum[i] + number
            prefix_digits[i + 1] = (prefix_digits[i] * 10 + number) % MOD if number else prefix_digits[i]
            prefix_count[i + 1] = prefix_count[i] + (1 if number else 0)

        for l, r in queries:
            r += 1

            s = prefix_sum[r] - prefix_sum[l] # good to go
            x = (prefix_digits[r] - prefix_digits[l] * pow[prefix_count[r] - prefix_count[l]])

            res.append(x*s%MOD)
            
        return res
