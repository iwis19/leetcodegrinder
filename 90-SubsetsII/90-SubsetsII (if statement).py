class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        """
        not using sets, using a check, will MAKE SURE TO READ THE REASONING TOMORROW.

        need to get better at these checks, but now i know do not use sets as theyre inefficient even tho theyre o(1) lookup, recursion brings too much burden

        0 ms runtime beats 100% 
        """
        
        nums.sort()
        res = []
        n = len(nums)

        def dfs(start, prev_arr):

            res.append(prev_arr[:])
                
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue

                prev_arr.append(nums[i])
                dfs(i+1, prev_arr)
                prev_arr.pop()

        dfs(0, [])

        return res
