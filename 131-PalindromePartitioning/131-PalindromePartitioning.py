class Solution:
    def partition(self, s: str) -> list[list[str]]:
        
        n = len(s)

        if n == 1:
            return [[s]]

        """
        original:
        just go thru all partitions and see if p == p[::-1]?

        since s.length is max 16, that means we have max 16 cuts to make. i think we can do a backtrack partition where we begin by cutting into 2 pieces, then branching off into 3, 4, 5 ... etc

        note that all len 1 partitioned strings are palindromes

        afterwards:
        original idea was pretty correct in general, just instead of splicing into 3,4,5 was somewhat a bit off. all i had to do i sjust keep forlooping and splicing from the left (from wherever i left off at) and once teh entire thing was split into palindromic parts i just return.

        had a quick bug on indexing but realized the exclusivity on splicing indices so fixed quickly, good debugging practice

        41 ms runtime beats 67%
        """

        res = []

        def dfs(arr, i):
            
            """
            lowkey just do a loop and keep breaking down the words and then keep going
            """
            if i == n:
                res.append(arr[:])

            for j in range(i+1, n+1):
                piece = s[i:j]
                if piece == piece[::-1]:
                    arr.append(piece)
                    dfs(arr, j)
                    arr.pop()

        dfs([], 0)

        return res
