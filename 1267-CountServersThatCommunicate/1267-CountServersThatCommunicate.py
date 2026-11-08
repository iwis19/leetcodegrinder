class Solution:
    def countServers(self, grid: list[list[int]]) -> int:

        """
        im actually BUGGING no way i spent this long on this brainless set problem

        mistakes:
        1. accidentally added row # to the set thats supposed to contain cols index (per row set)
        2. did the same as 1 but for col sets
        3. checked for len > 1 when i or j is alr in it and then proceeded to use an or to wipe it out. i had like
        or (len > 0) which is literally prolly always true and the prev check holds no meaning then
        4. im just dum not much to frigging say
        5. after a little bit i also js realized i did all that comparison statements for nothing it wasnt evenneeded it was so dumb because the numbers are alr guaranteed to have their i in the col set and j in row set ...

        15 ms runtime beats 78%
        """
        
        m, n = len(grid), len(grid[0])
        rows = [set() for _ in range(m)]
        cols = [set() for _ in range(n)]
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows[i].add(j)
                    cols[j].add(i)

        for i in range(m):
            for j in range(n):
                if grid[i][j] and (len(rows[i]) > 1 or len(cols[j]) > 1):
                    ans += 1

        return ans
