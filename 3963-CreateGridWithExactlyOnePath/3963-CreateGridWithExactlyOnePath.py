class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:

        """
        daily
        """
        
        grid = [ ["#"] * n for _ in range(m) ]

        for i in range(n):
            grid[0][i] = "."

        for i in range(m):
            grid[i][-1] = "."

        for i in range(m):
            row = "".join(grid[i])
            grid[i] = row

        return grid
