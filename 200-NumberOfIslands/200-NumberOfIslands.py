class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        """
        same idea as 695, put each visited to -1

        only go to potential islands and clean them up

        was bugging for 20 minutes because i didnt knwo the inputs were str instead of ints like #695????

        230ms runtime beats 88%
        """

        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(row, col):
            grid[row][col] = "-1"
            if row+1 < rows and grid[row+1][col] == "1": dfs(row+1, col)
            if row-1 > -1 and grid[row-1][col] == "1": dfs(row-1, col)
            if col+1 < cols and grid[row][col+1] == "1": dfs(row, col+1)
            if col-1 > -1 and grid[row][col-1] == "1": dfs(row, col-1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    res += 1
                    dfs(row, col)

        return res

        
