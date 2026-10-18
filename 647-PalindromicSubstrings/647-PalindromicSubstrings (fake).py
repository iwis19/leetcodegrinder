class Solution:
    def countSubstrings(self, s: str) -> int:

        """
        retarded solution

        700+ ms runtime beats 8%
        """
        
        # find all substrings

        n = len(s)
        ctr = 0

        for i in range(n):
            for j in range(i, n):
                string = s[i:j+1]
                if string == string[::-1]:
                    ctr += 1

        return ctr
