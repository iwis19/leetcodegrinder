class Solution:
    def numberOfSpecialChars(self, word: str, ans = 0) -> int:

        """
        originally wanted to just modify the part I solution, but realized it was too complicated to do so.

        scrapped and decided to track indices of each upper and lower indices, but lead to complicated checking logic when it came down to checking those 0 and 1s

        submitted, 355 ms, beats only 15% so looked at leetcode analysis and learned to keep just last lower index and dfirst upper index.

        now 320 ms runtime beats 22%.

        the 55 ms solution is essentially using rfind and find, which is the same idea but simply more efficient.
        """
        
        last_lower, first_upper = [-1] * 26, [-1] * 26

        for i in range(len(word)):

            letter = word[i]
            id = ord(letter.lower()) - ord('a')

            if letter.islower():
                last_lower[id] = i
            else:
                if first_upper[id] == -1:
                    first_upper[id] = i

        count = 0

        for i in range(26):
            if last_lower[i] != -1 and first_upper[i] != -1 and last_lower[i] < first_upper[i]:
                count += 1

        return count
