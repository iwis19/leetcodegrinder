class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        """
        use the grid itself as a seen counter. since its only 1 and 0s,
        i set visited cells to -1.

        in a dfs, we can only travel 4 directions: top, bottom, left, right
        only increase area if we find a 1

        needed a bit of hint since it was my first time, but the dfs algo was fully myself kinda proud haha 

        # of islands next.

        21 ms runtime beats 44%
        """

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(row, col):
            if not (0 <= row < rows and 0 <= col < cols):
                return 0

            if grid[row][col] == -1 or grid[row][col] == 0:
                return 0

            grid[row][col] = -1

            return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(dfs(row, col), max_area)
                grid[row][col] = -1

        return max_area
