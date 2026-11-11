class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        """
        douggie put me on with assignment #4

        also learned that i could just use @cache and not use memo python is goated

        but memo in dp basically stores the call arguments (since no global vars are depended on / edited anyw), and then we just call it again to reuse instead of calculating / making more branches

        38 ms runtime beats 80%
        """

        n1, n2 = len(word1), len(word2)

        memo = {}
        
        def dp(i1, i2):

            if i1 == n1:
                return n2 - i2

            if i2 == n2:
                return n1 - i1

            if (i1, i2) in memo:
                return memo[(i1,i2)]

            if word1[i1] == word2[i2]:
                if (i1+1, i2+1) in memo:
                    return memo[(i1+1, i2+1)]

                memo[(i1+1, i2+1)] = dp(i1+1, i2+1)
                return memo[(i1+1, i2+1)]

            memo[(i1, i2)] = 1 + min(dp(i1+1, i2), dp(i1, i2+1), dp(i1+1, i2+1))
            return memo[(i1, i2)]

        return dp(0, 0)
