class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        """
        backtracking goattttt

        0 ms runtime beats 100%
        """

        res = []
        n = len(nums)
        
        def dfs(visited, prev):

            if len(prev) == n:
                res.append(prev[:])
                return

            for i in range(n):
                if i in visited:
                    continue
                prev.append(nums[i])
                visited.add(i)
                dfs(visited, prev)
                visited.discard(i)
                prev.pop()

        dfs(set(), [])

        return res

