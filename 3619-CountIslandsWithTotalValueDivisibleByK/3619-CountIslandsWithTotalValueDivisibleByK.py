class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:

        """
        im genuinely bugging bro wtf

        also thought my approach was hot fucking ass but turns out i js had a debugging print statement

        325ms runtime beats 64%, lowkey did not think actually returnign would work better here than the update
        res appraoch i did for # of islands
        """
        
        ans = 0
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            
            if (not 0<=i<m) or (not 0<=j<n) or (not grid[i][j]):
                return 0

            temp = grid[i][j]
            grid[i][j] = 0
            total = temp + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j-1) + dfs(i, j+1)
            
            return total

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and not dfs(i, j) % k:
                    ans += 1

        return ans


        
