class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        """
        genuinely bbbugging

        0 ms runtime beats 100%
        """
        
        if obstacleGrid[0][0]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        grid = [ [0] * n for _ in range(m) ]
        grid[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue

                if obstacleGrid[i][j]:
                    continue

                left = up = 0
                if i-1 >= 0:
                    up = grid[i-1][j]
                if j-1 >= 0:
                    left = grid[i][j-1]
                    
                grid[i][j] = left + up

        return grid[m-1][n-1]
