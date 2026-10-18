class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:

        """
        it was during contest, readding now

        237 ms runtime beats 92%
        """

        m, n = len(grid), len(grid[0])

        visited = [ [False] * n for _ in range(m) ]
        r,c = 0, 0
        visited[r][c] = True

        while True:

            if grid[r][c] == 'L' and c-1 >= 0 and not visited[r][c-1]:
                visited[r][c-1] = True
                c-=1
            elif grid[r][c] == 'R' and c+1 < n and not visited[r][c+1]:
                visited[r][c+1] = True
                c+=1
            elif grid[r][c] == 'U' and r-1 >= 0 and not visited[r-1][c]:
                visited[r-1][c] = True
                r-=1
            elif grid[r][c] == 'D' and r+1 < m and not visited[r+1][c]:
                visited[r+1][c] = True
                r+=1
            else:
                break

        return [r,c]
                
                

        
