class Solution:
    def totalNQueens(self, n: int) -> int:

        """
        had some oofy moments with indices but we pulled thru 

        4 ms runtime beats 93%
        """
        
        pos_diag = [False] * (2*n-1)
        neg_diag = [False] * (2*n-1)
        cols = [False] * n
        ans = 0

        def dfs(i):   # depth reached with rows
            nonlocal ans

            if i == n:
                ans += 1
                return

            for j in range(n):
                if not cols[j] and not pos_diag[i+j] and not neg_diag[i-j+(n-1)]:
                    neg_diag[i-j+(n-1)] = True
                    pos_diag[i+j] = True
                    cols[j] = True
                    dfs(i+1)
                    neg_diag[i-j+(n-1)] = False
                    pos_diag[i+j] = False
                    cols[j] = False

        dfs(0)
        return ans
