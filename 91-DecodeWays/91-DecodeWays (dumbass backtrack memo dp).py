class Solution:
    def numDecodings(self, s: str) -> int:
        
        """
        backtracking problem  -> NO IT WAS DP

        - cant start with a zero
        - cant go above 26

        or i can just pass in an index i, and then i just check what happens when i take s[i:i+1] and s[i:i+2] (if possible)
        * when next is a 0, it must be included (cant do single)

        basecase:

        if next dig isnt 0:
        count += dfs(i+1)
        
        if enough digs left, and the splice gives less than 26
        count += dfs(i+2)

        bro oops i accidentally worked on ho wmany things it can be partitioned into

        1 ms runtime beats 42%
        """

        n = len(s)

        @cache  # because after i reach dfs(i), wtv happens in dfs(i+1) or dfs(i+2) applies to all cases of dfs(i)
        def dfs(i):

            if i == n:
                return 1

            if s[i] == "0":
                return 0

            count = 0
                
            if (i+1 < n and s[i+1] != "0") or (i == n-1):
                count += dfs(i+1)
            
            if (i+1 < n and int(s[i:i+2]) <= 26):
                count += dfs(i+2)

            return count

        return dfs(0)
