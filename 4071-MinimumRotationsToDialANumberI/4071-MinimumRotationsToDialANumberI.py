class Solution:
    def minRotations(self, s: str) -> int:

        """
        did all this by myself but codex helped me realize abs() works better instead of how i used to just check for pos/neg

        0 ms runtime beats 100%
        """

        def minRotation(curr, goal) -> int:
            return min(10 - abs(curr - goal), abs(curr - goal))

        curr = 0
        res = 0
        
        for num in s:
            res += minRotation(int(curr), int(num))
            curr = num

        return res
