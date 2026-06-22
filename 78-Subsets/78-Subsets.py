class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        """
        had a late night brainf art...

        0 ms runtime beats 100%
        """

        res = []
        n = len(nums)
        
        def dfs(start, prev_arr):

            res.append(prev_arr[:])

            for i in range(start, n):
                
                print(f"current: {prev_arr}, boutta add: {nums[i]}, start is gonna be: {start+1}")
                prev_arr.append(nums[i])
                dfs(i + 1, prev_arr)
                prev_arr.pop()

        dfs(0, [])

        return res
