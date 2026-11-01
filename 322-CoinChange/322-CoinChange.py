class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        """
        bro my dumbass tried to do greedy

        this SHIT IS SO HARD WHAT THE FUCK

        438 ms runtime beats 91%
        """
        n = amount+1
        dp = [math.inf] * (n)
        dp[0] = 0

        for i in range(1, n):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i-coin])

        return dp[n-1] if dp[n-1] != math.inf else -1
            
        
            
        
            
