class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        """
        trying out some dfs and backtracking in matrices :)

        was very hard for me tbh, i had a general idea that i had to backtrack since this is just another search problem like path sum yesterday
        took a glance at solution, got the idea and coded it
        the 1st attempt code was better than i thought, although i got tle. turns out i could just track which index of hte word i am on in each call,
        as i originally kept an array of the letters, and joined it every dfs call to see if words were equal. 

        with the implementation i had to change to, i had to stop use True in the logics, but use True only for at the start (see the in-code comment)
        "yes this entire word matched" -> but it still worked fine as it was basically the same idea. neither True/false would be returned in order to proceed

        4036 ms runtime beats 45% pretty sure leetcode is lagging atm
        """
        
        visited = set()
        m, n = len(board), len(board[0])
        l = len(word)

        def dfs(r, c, i):    # for pos in the main program call, im gonna go thru board and find all occurrences of 1st letter in word to start scan

            # main goal: find out how to backtrack to last time i HAD to make a choice between all

            if i == l:
                return True              

            """
            conditions that one would fail:

            - r/c out of bounds
            - currently at a visited square
            -  ( NEVER HAVE TO WORRY ABOUT TOO LONG / TOO SHORT SINCE IF LEN OF PASSED IN PROCESS IS EQUAL TO I, WE ARE GOOD)
            """

            if (r, c) in visited or not (-1 < r < m) or not (-1 < c < n) or board[r][c] != word[i]:
                return False

            visited.add((r,c))

            res = dfs(r+1, c, i+1) or dfs(r, c+1, i+1) or dfs(r-1, c, i+1) or dfs(r, c-1, i+1)

            visited.remove((r,c))
            
            return res

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False

