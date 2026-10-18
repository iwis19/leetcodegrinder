class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        
        """
        it is important to note that the min val to travel to grid[i][j] is:

        min(path_sum[i-1][j], path_sum[i][j-1]) + grid[i][j]

        w thoughts w debugging L code style tho im pretty sure (realized its cleaner to take out i==0 and j==0 logic + do in separate loops)
        this is the cleaned up version rn, also removed the extra O(mxn) space extra path sum array for space complexity

        8 ms runtime beats 70%
        """

        m,n = len(grid), len(grid[0])

        # for first col
        for i in range(1, m): grid[i][0] += grid[i-1][0]

        # for first row
        for j in range(1, n): grid[0][j] += grid[0][j-1]

        for i in range(1, m):
            for j in range(1, n):
        
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]) 

        return grid[m-1][n-1]
