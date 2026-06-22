class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:

        """
        mmm good one

        need to be more flexible, not just break or continue, but use return to break out of any amts of loops i want

        0 ms runtime beats 100%
        """
        
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        res = 0

        while True:
            for c in target:
                if freq[ord(c) - ord('a')] == 0:
                    return res
                freq[ord(c) - ord('a')] -= 1

            res += 1

        return None
