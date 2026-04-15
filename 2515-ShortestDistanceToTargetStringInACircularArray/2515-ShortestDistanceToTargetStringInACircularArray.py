class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:

        """
        another daily horay

        0 ms runtime beats 100
        """
        
        n = len(words)
        
        if words[startIndex] == target: return 0

        start = startIndex
        for i in range(n):

            next_word = words[(start + i) % n]
            prev_word = words[(start - i) % n]

            if next_word == target or prev_word == target:
                return i

        return -1
