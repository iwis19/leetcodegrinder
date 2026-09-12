class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:

        """
        original thought process
        like spiral matrix I and II, perform traversals in order: left, down, right, up

        for each direction, if it goes out of bounds, i lock it and i swap directions again

        i dont think i even need to do the above i can just simply check every coord if its inbounds or nah

        pattern:
        left: 1 down: 1 right: 2 up: 2
        left: 3 down: 3 right: 4 up: 4

        overall good thought process, good execution, reasonable amt of time taken, suggested TC as well but has a better math oriented sol so will try it out now

        12 ms runtime beats 40%
        """
        
        total = rows * cols
        
        res = [[rStart, cStart]]

        # bounds
        top, bottom = 0, rows-1
        left, right = 0, cols-1

        def add_to_res(row, col):
            if (left <= col <= right) and (top <= row <= bottom):
                res.append([row, col])

        col, row = cStart, rStart
        step_count = 1    # incr by 1 every 2 directional changes

        while len(res) < total:

            # left
            for _ in range(step_count):
                col += 1
                add_to_res(row, col)

            # down
            for _ in range(step_count):
                row += 1
                add_to_res(row, col)

            step_count += 1

            # right
            for _ in range(step_count):
                col -= 1
                add_to_res(row, col)

            # up
            for _ in range(step_count):
                row -= 1
                add_to_res(row, col)

            step_count += 1

        return res

