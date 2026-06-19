class Solution:
    def combinationSum(self, c: List[int], t: int) -> List[List[int]]:

        """
        definitely still learning dfs and backtracking, had MOST OF IT DOWN THIS TIME THO

        just missed the concept of sorting the candidates and having a set start -> very effectively eliminates duplicated results for questions who needs those distinct outputs e.g. [2,3,3] and [3,2,3]

        using start would prevent going backwards in the list, now we may only hve outputs in sorted smallest -> biggest order.

        e.g. where c = [2,3,6,7] and then im currently at 6. i could go back and get a 2 + 3 but that has already been accessed and added to res, if it wasnt sorted and pruned and had a set start, then i wouldnt eject this choice

        2 ms runtime beats 96%
        """

        c.sort()
        
        res = []
        n = len(c)

        def dfs(start, remaining, prev):

            if remaining == 0:
                res.append(prev[:])
                return

            for i in range(start, n):
                num = c[i]
                if remaining - num < 0:
                    return
                prev.append(num)
                dfs(i, remaining - num, prev)
                prev.pop()

        dfs(0, t, [])
        
        return res
