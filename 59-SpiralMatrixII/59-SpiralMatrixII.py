class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        """
        lesss gooo, could also do dx, dy = -dy, dx from matrix rotation m,ethod

        0 ms runtime beats 100%
        """
        
        res = [[0 for j in range(n)] for i in range(n)]

        top, left = 0, 0
        bottom, right = n, n
        v = 1

        while top < bottom and left < right:

            for i in range(left, right):
                res[top][i] = v
                v += 1
            top += 1

            for i in range(top, bottom):
                res[i][right - 1] = v
                v += 1
            right -= 1

            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    res[bottom - 1][i] = v
                    v += 1
                bottom -= 1

            if left < right:
                for i in range(bottom - 1, top - 1, -1):
                    res[i][left] = v
                    v += 1
                left += 1

        return res

