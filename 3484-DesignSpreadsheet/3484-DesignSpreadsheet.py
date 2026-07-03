class Spreadsheet:

    """
    used array instead of hashtable. also needed a littel bit of help on getValue implementation but other things were fine ig
    
    didnt really realize how map wouldve been better in this situation (way better) bc most cells are never used so i just set the ones that will exist.

    kinda counterintuitive but makes sense. i dont need all the blocks in the world since im not displaying anything

    super slow 164 ms runtime beats 22%
    """

    def __init__(self, rows: int):
        self.spreadsheet = [[0] * _ for i in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        row, col = self.getRowCol(cell)
        self.spreadsheet[row][col] = value
        
    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        eq = formula[1:]
        for i in range(len(eq)):
            if eq[i] == '+':
                e1, e2 = eq[:i], eq[i+1:]  # expression 1, expression 2
                if 65 <= ord(e1[0]) <= 90:
                    r, c = self.getRowCol(e1)
                    v1 = self.spreadsheet[r][c]
                else:
                    v1 = int(e1)
                if 65 <= ord(e2[0]) <= 90:
                    r, c = self.getRowCol(e2)
                    v2 = self.spreadsheet[r][c]
                else:
                    v2 = int(e2)
                return v1 + v2
    
    def getRowCol(self, cell: str) -> tuple[int, int]:
        col = ord(cell[0]) - 65   # 0 indexed
        row = int(cell[1:]) - 1  # 1 indexed, but we -1 to get 0 indexed

        return row, col   # row col
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
