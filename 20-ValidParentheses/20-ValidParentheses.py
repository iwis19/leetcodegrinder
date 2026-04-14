class Solution:
    def isValid(self, s: str) -> bool:

        """
        solves in O(n)

        1. think i saw solution somewhere else a long long time ago but solved it by myself
        2. uses map and a stack

        0 ms runtime beats 100
        """

        # use a stack

        map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }


        # keep going thru the brackets in s and append each of them into 
        # a stack, when an closing bracket is encountered, i check if the counter part
        # (opening bracket) is the last of the stack, if not, then i return false
        
        stack = []
        
        for bracket in s:
            
            # opening brackets
            if bracket not in map:
                stack.append(bracket)
                continue

            # closing brackets
            if not stack or map[bracket] != stack[-1]:
                return False
            stack.pop(-1)
        
        return not stack
