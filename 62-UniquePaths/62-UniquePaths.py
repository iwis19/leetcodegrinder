class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        """
        got better at debugging

        had a good clue of this, solved it fairly quick. essentially pascals triangle / fibonacci (dp)

        0 ms runtime beats 100%
        """
        
        paths = [ [1] * n for _ in range(m) ]

        # find a way to work in diagonals / or i can just go in rows

        for row in range(1, m):
            for col in range(1, n):

                if row == col == 0:
                    continue
                
                above, left = 0, 0
                # check row-1 and col-1
                if 0 <= row-1:
                    above = paths[row-1][col]
                if 0 <= col-1:
                    left = paths[row][col-1]

                paths[row][col] = above + left

        return paths[-1][-1]
