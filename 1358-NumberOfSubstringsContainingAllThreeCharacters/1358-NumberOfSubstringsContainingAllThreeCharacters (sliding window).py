class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        """
        still dont really understand this sliding window thing, but will def learn it soon.

        143 ms runtime beats 16%
        """
        
        res = 0
        n = len(s)
        l, r = 0, 0
        arr = [0, 0, 0]

        while r < n:
            arr[ord(s[r]) - ord('a')] += 1

            while self.has_all_chars(arr):
                res += n - r

                arr[ord(s[l]) - ord('a')] -= 1
                l += 1

            r += 1
        
        return res

    def has_all_chars(self, arr):
        return min(arr) != 0
