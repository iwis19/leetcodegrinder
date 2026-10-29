class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        """
        HORAY 100/150 NEETCODE 150!!!!

        7 ms runtime beats 50%, can be optimized here
        """

        m,n = len(board), len(board[0])
        safe = set()

        def dfs(i, j):

            stuck = True
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                newi, newj = i+di, j+dj

                if (newi, newj) not in safe and -1<newi<m and -1<newj<n and board[newi][newj] == "O":
                    stuck = False
                    safe.add((newi, newj))
                    dfs(newi, newj)

            if stuck:
                return

        # run dfs algo, add all connected to set, and we do another loop through entire matrix to set all boxes that are "O" and arent in this set.
                    
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m-1 or j == 0 or j == n-1) and board[i][j] == "O":
                    safe.add((i,j))
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in safe:
                    board[i][j] = "X"


                    

            

        
