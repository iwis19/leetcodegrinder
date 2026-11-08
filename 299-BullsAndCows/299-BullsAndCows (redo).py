class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        """
        guess what pal im back and i thought of this sol and i did it in 5 mins !!!!!
        """
        
        n = len(secret)
        A = 0
        s = {}
        g = {}

        for i in range(n):
            if secret[i] == guess[i]:
                A += 1
            else:
                s[secret[i]] = s.get(secret[i], 0) + 1
                g[guess[i]] = g.get(guess[i], 0) + 1

        B = 0

        for key, value in g.items():
            
            # take take min(value in s, value)
            s_value = 0
            if key in s:
                s_value = s[key]

            B += min(value, s_value)

        return f"{A}A{B}B"

            
            
