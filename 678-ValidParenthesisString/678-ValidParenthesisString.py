class Solution:
    def checkValidString(self, s: str) -> bool:
        wildcard = []
        stack = []  # to store reg bracks, but im gonna store them as tuples to see if the wild card was before or after

        """
        Holy shit i thought this was a lot shorter but it was goooooood

        0 ms runtime beats 100%
        """

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == "*":
                wildcard.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    if not wildcard:
                        return False
                    else:
                        wildcard.pop()

        # check the remaining leftside ( brackets, since the wildcard i is already sorted
        
        # early exit
        if not stack:
            return True

        """
        CORE: stack[i][1] < wildcard_i
        not every wild card needs to be used up. but if stack[i][1] doesnt satisfy the rule above,
        then it wont satisfy any other wildcard anyway, and hence we return false
        """
        i = j = 0

        while j < len(wildcard) and i < len(stack):
            if stack[i] < wildcard[j]:
                i+=1
            j += 1
        
        return i >= len(stack)

                
        


        
