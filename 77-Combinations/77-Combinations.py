class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        
        nums = [ i for i in range(1, n+1) ] # length n
        res = []

        """
        well i had a quick impl for first run, then got the hint to optimize

        took some time to fucking fix the indexing like everything was right and i thought i had a return
        and i ran it so many times and it was false but turns out i just didnt have the correct bounds and the return
        in the code at the same time??????????

        84 ms runtime beats 86%
        """

        # no need to pass in start_index because i can get it from the last element
        def dfs(curr, start):

            l = len(curr)

            if l == k:
                res.append(curr[:])
                return

            """
            say that i am currently at l = 2, but i need k = 4.
            i need k-l more elements, therefore my last loop should end at n-(k-l-1)
            """

            for i in range(start, n-k+l+1):
                curr.append(nums[i])
                dfs(curr, i+1)
                curr.pop()

        dfs([], 0)
        
        return res


            

            

            
