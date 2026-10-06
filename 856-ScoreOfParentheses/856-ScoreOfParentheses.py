class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        """
        original:
        need to start from popping the very insides

        using a stack + how many opens, i can tell how many layers wrapped inside this is
        but that isnt sufficient because its not the more inside the better, its the more outside the more points.
        when popped, i need to keep a sum of the amt of POINTS that alr happened inside

        if i (close brack) == i (open brack) + 1, then the point defaults to 1
        else, point has to be calculated as 2 * (total cnt of pts inside)

        maybe a scan at start and start from the last start brack?

        i need to keep tracking where each start brack is closed s.t. i can keep going inside and find total pts inside

        the s.length is 50 so i might be able to do this without tle

        after:
        needed a slight nudge from jipiti, all impl + debugging by myself

        good problem

        0 ms runtime beats 100%
        """

        # keep this extra 0 index to prevent final result from getting popped + place for storage
        stack = [[0, 0]]

        for i, brack in enumerate(s):

            if brack == "(":
                stack.append([i, 0])  # the second number is the running inner sum

            elif brack == ")":
                
                open_i, inner_sum = stack.pop()

                # nothing inside
                if open_i + 1 == i:
                    inner_sum += 1
                # otherwise
                else:
                    inner_sum *= 2

                stack[-1][1] += inner_sum

        return stack[0][1]
