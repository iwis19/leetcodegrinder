class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        """
        bruh i thought there was a catch to this

        0 ms runtime beats 100%
        """
        
        stack = []

        res = 0

        for i, brack in enumerate(s):

            if brack == "(":
                stack.append(i)

            elif brack == ")":
                if stack:
                    stack.pop()
                    continue
                res += 1

        res += len(stack)

        return res
