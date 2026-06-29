class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:

        """
        oh ok
        """
        
        res = 0

        for pattern in patterns:

            if pattern in word:
                res += 1

        return res
