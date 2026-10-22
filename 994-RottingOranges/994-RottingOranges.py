class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        
        """
        since max(m*n) = 100, we can run simulation

        some conditions:
        - if all rotten oranges cant expand in ANY direction, return -1 -> maybe keep an updated list on spreadable rotten oranges
        - when all oranges are rotten, we return time

        keep an updated list of rotten oranges per iteration so that i dont make the NEW rotten oranges rot something as well
        
        2 ms runtime beats 82%
        """

        time = 0
        rottens = set()
        freshes = set()

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: rottens.add((i,j))
                elif grid[i][j] == 1: freshes.add((i,j))

        while len(freshes) > 0:
            time += 1
            new_rottens = set()
            for x,y in rottens:
                if (x+1,y) in freshes:
                    new_rottens.add((x+1,y))
                    freshes.discard((x+1,y))
                if (x-1,y) in freshes:
                    new_rottens.add((x-1,y))
                    freshes.discard((x-1,y))
                if (x,y+1) in freshes:
                    new_rottens.add((x,y+1))
                    freshes.discard((x,y+1))
                if (x,y-1) in freshes:
                    new_rottens.add((x,y-1))
                    freshes.discard((x,y-1))
            
            if not new_rottens:
                return -1

            rottens.update(new_rottens)

        return time

994
