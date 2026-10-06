class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if haystack == needle:
            return 0
        
        n = len(needle)
        m = len(haystack)

        if m < n:
            return -1

        for i in range(m):
            if haystack[i : i+n] == needle:

                return i

        return -1
