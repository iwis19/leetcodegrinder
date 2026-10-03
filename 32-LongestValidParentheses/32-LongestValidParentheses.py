class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        if not s:
            return 0

        stack = []
        last_invalid = -1

        res = 0
        i = 0
        n = len(s)

        """
        original:
        i think the idea is just to keep simulating down s until a point where the sequence / stack becomes invalid
            - when that happens, do max(res, curr)

        the bigger issue is: how do i know how long (((())) gives us in hindsight? i know that it is 6 but how do i identify that it is 6 after ive hit the point of failure?

        i think the thing is that all the way up until (((())) (before next char _), we know its valid. therefore the only possible reason for this to end up being invalid is that were missing the closings. this idea applies to all cases since a sequence can be considered valid until something goes wrong, and that issue has to stem from a missing closing bracket as we can start however we want aka opening brackets.

        ill keep a counter on how many closing brackets i have in the sequence.
        
        what about ((())((? how could i tell that the valid result is 4? this entire sequence has 7 and is considered temporarily valid... but the closing bracket count * 2 still works?


        after:
        wrote good skeleton, had a good idea in mind and wrote down some cases that i thought would be good to solve before coding
        
        the test case ()(() stomped original sol, and ai helped me realize that i could just keep a valid run length in every iteration. e.g. i would realize that s[2] = "(" would break my current length, giving me only i=4 - i=2 = 2 max length. i will anticipate that a ")" eventually comes to close this s[2] = "(" by keeping a var called last_invalid s.t. i could bring back the prev valid sequences as a count, but not until the stack becomes empty (meaning s[2] has been taken away by an ").")

        9 ms runtime beats 52%
        """

        for i in range(n):

            brack = s[i]
        
            # if open brack:
            if brack == "(":
                stack.append(i)
            
            # else if close brack:
            if brack == ")":
                # broken case
                if not stack:
                    last_invalid = i

                else:
                    stack.pop()

                    if stack:
                        res = max(res, i - stack[-1])

                    else:
                        res = max(res, i - last_invalid)

        return res
