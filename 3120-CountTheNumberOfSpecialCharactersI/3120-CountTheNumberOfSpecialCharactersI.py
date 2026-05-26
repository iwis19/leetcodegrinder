class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        

        lower, upper = [0] * 26, [0] * 26
        count = 0

        for char in word:
            if char.islower():
                lower[ord(char) - ord('a')] += 1
            else:
                upper[ord(char) - ord('A')] += 1

        for i in range(26):
            if lower[i] != 0 and upper[i] != 0:
                count += 1

        return count

