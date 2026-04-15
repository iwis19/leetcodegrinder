class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        # each time i turn, i increment horizontal/vertical gap based on what direction i just went in
        # this is because through spiraling, the dist i can travel in each direction decreases by 1 each time

        # m is amt of rows, n is amt of cols
        m, n = len(matrix), len(matrix[0])
        res = []
        # x related -> col, y related -> row
        x, y, gap_x, gap_y = 0, 0, 0, 0

        # imagine example 1, r = 3, c = 3
        while gap_x < n and gap_y < m:
            
            # move right
            while x < n - gap_x:
                # this is matrix[y][x] as y is essentially the rows, x is essentially the cols
                res.append(matrix[y][x])
                x += 1
            gap_x += 1
            gap_y += 1

            # move down
            while y < m - gap_y:
                res.append(matrix[y][x])
                y += 1
            

            # move left
            while x >= 0:
                res.append(matrix[y][x])
                x -= 1
            gap_x += 1
            gap_y += 1

            # move up
            while y >= 0:
                res.append(matrix[y][x])
                y -= 1

        return res


        
