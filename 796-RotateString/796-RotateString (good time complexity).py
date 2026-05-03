class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        """
        i definitely thought about checking for cycles, but i didnt think of this directly. still somehwat proud of thinking about cycles but yeah i guess 
        i still needed a hint on this

        0 ms runtime beats 100%
        """
        
        if len(s) != len(goal): return False

        return goal in (s+s)
