class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        
        """
        had the right general idea of backtracking + a lot of details, but missed:
        - r+c and r-c tells me which diagonal pos(r,c) belonged in
        - since i only run this dfs once, i can keep the sets and arrays in the method (not passed each time in dfs)
        - created a copy each time i called dfs recursively, when i only needed it for appending to res
        - for some reason also thought i needed a set for rows, but i was already going down by rows

        7-12 ms runtime beats 66-97%
        """

        if n == 1:
            return [["Q"]]

        if n == 2 or n == 3:
            return []

        res = []

        def dfs(r):  # arr is a full nxn array filled with empty dots
            
            # base case: fully done, append arr to res (no need to check as its checked beforehand)
            if r == n:
                copy = arr[:]
                res.append( [ "".join(copy[row]) for row in range(n) ] )
                return

            # process queen placements from top to bottom row by row
                # if dont work, i return empty and end this
                    # check for: nearby, same col, same row
                # if works, i pass it down again

            # iterate through cols
            for c in range(n):
                if c in taken_cols or r+c in taken_pos_diag or r-c in taken_neg_diag:   # 1 more or
                    continue
                
                arr[r][c] = "Q"
                taken_cols.add(c)
                taken_pos_diag.add(r+c)
                taken_neg_diag.add(r-c)

                dfs(r+1)

                arr[r][c] = "."
                taken_cols.remove(c)
                taken_pos_diag.remove(r+c)
                taken_neg_diag.remove(r-c)
        
        taken_cols = set()
        taken_pos_diag = set()    # positive slope y=x diagonal, notice that all r+c is the same for each diag
        taken_neg_diag = set()    # negfative slope y=-x diagonal, notice that all r-c is the same for each diag
        arr = [ ["."] * n for _ in range(n) ]

        dfs(0)

        return res
