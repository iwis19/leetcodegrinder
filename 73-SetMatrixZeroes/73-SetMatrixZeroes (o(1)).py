class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        """
        took way too long to solve because i decided to go for O(1) solution first go and oversaw the use of booleans, then tried and overcomplicated
        things.

        i se em to have a trend of overcomplicating problems just because they look hard. i can come up with more modular logic, whether that is simply
        using more loops, even like 6, or writing a very simple logic / helper, etc.

        1 ms runtime beats 94% O(1) space
        """
        
        # iterate through the entire matrix and set matrix[row][0] and matrix[0][col] to "" as a marking
        # and then just use a for loop to go through first row and first col and set those values to 0
        m, n = len(matrix), len(matrix[0])
        firstrowzero = False
        firstcolzero = False

        for row in range(m):
            if matrix[row][0] == 0:
                firstcolzero = True
                break

        for col in range(n):
            if matrix[0][col] == 0:
                firstrowzero = True
                break

        # row
        for row in range(1,m):
            # col
            for col in range(1,n):

                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        # go thru each col and make the remainder of the col 0s
        for col in range(1,n):
            if matrix[0][col] == 0:
                for row in range(1,m):
                    matrix[row][col] = 0

        # go thru each row and make the remainder of the row 0s
        for row in range(1,m):
            if matrix[row][0] == 0:
                for col in range(1,n): 
                    matrix[row][col] = 0

        # make the first row all 0s
        if firstrowzero:
            for col in range(n):
                matrix[0][col] = 0

        # make the first col all 0s
        if firstcolzero:
            for row in range(m):
                matrix[row][0] = 0










                    
        

        

        


