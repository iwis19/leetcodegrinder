class Solution:
    def numDecodings(self, s: str) -> int:
        
        """
        that was SO stupid of me to think it was a bp problem at 100

        essentially how many ways there are to reach index i, and we eventually make it to index i == n-1

        good dp sol, needed a lot of logic and brain
        
        0 ms runtime beats 100%
        """

        if s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1 # can reach zero char AND first char obv  dp[i] -> however many ways to reach length i. 1 indexed.

        for i in range(2, n+1):
            
            if s[i-1] != "0":  # since theres dp[i-1] many ways to get to i-1, we still cant progress if i-1 is 0. not i.
                dp[i] += dp[i-1]

            if i-2 >= 0 and 10 <= int(s[i-2:i]) <= 26:  # dp[i-2] ways to hit i-2, still need to check i-2, i-1 combined num
                dp[i] += dp[i-2]

        return dp[n]
