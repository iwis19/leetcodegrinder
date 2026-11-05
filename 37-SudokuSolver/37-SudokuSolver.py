class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        """
        mainly just need to trial and error, put in one number if nothing else fails and go by the rows. hold 
        three lists of sets: row, col, box. use indices to figure out which one they are.

        1, 1 -> int div row by 3, int div col by 3, get 0, 0 then 3*0+0 = square 0
        4, 4 -> int div row by 3, and int div col by 3, u get square 1, 1; and then 3*row+col = square 4.
        7, 7 -> 2, 2; 3*2+2 = square 8 -> last square

        jeez i just sat here like debugged 30 bugs and i needed help on the very last
        1. cant do [set()] * 9 like an int / basic data type
        2. conceptualizing // and %
        3. forgot to fill row col box sets before running dfs
        4. wrong base case coords at the start

        WORST MISTAKE:
        - forgot that return only exits the highest call, it would go back and keep executing everything else so even when
        i have obtained a full sol, without returning True, I essentially just deleted all of my solutions off the board
        and returned an empty one...

        2474 ms runtime beats 31% -> sets
        1204 ms runtime beats 62% -> arrays size 9
        """

        rows = [ [0] * 9 for _ in range(9)]
        cols = [ [0] * 9 for _ in range(9)]
        boxes = [ [0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])
                rows[i][num-1] = 1
                cols[j][num-1] = 1
                boxes[3*(i//3) + j//3][num-1] = 1

        def dfs(i, j):
            if i == 9 and j == 0:
                return True

            if board[i][j] != ".":
                return dfs(i + (j+1) // 9, (j+1) % 9)
            
            row, col, box = rows[i], cols[j], boxes[3*(i//3) + j//3]
            for num in range(1,10):
                if (not row[num-1]) and (not col[num-1]) and (not box[num-1]):
                    board[i][j] = str(num)
                    row[num-1] = 1
                    col[num-1] = 1
                    box[num-1] = 1
                    if dfs(i + (j+1) // 9, (j+1) % 9):
                        return True
                    row[num-1] = 0
                    col[num-1] = 0
                    box[num-1] = 0
                    board[i][j] = "."

            return False

        dfs(0,0)
