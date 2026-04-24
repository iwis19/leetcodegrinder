class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        """
        easy wow

        0 ms runtime beats 100
        """
        
        pos = 0
        free_move = 0
        for move in moves:
            if move == "_":
                free_move += 1
            elif move == "L":
                pos += 1
            elif move == "R":
                pos -= 1

        return abs(pos) + free_move
