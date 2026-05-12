class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        """
        maybe i got the hang of it from earlier tries of o(1), but o(m+n) seemed very easy to me

        O(m+n) space try
        """
        
        m, n = len(matrix), len(matrix[0])
        rowzeroes, colzeroes = set(), set()

        for row in range(m):

            for col in range(n):

                if matrix[row][col] == 0:
                    rowzeroes.add(row)
                    colzeroes.add(col)


        for row in rowzeroes:
            for col in range(n):
                matrix[row][col] = 0

        for col in colzeroes:
            for row in range(m):
                matrix[row][col] = 0


    
