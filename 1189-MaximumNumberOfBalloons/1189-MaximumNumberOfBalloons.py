class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        """
        easy one, made a dumb mistake on the way

        3 ms runtime beats 61%
        """

        res = math.inf
        
        freq = { 
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0
        }

        for char in text:
            if char not in freq:
                continue
            freq[char] += 1

        for key, val in freq.items():
            n = val // 2 if key == 'l' or key == 'o' else val
            res = min(res, n)

        return res
