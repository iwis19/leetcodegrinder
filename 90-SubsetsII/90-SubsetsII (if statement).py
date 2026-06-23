class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        """
        not using sets, using a check.

        uses i > start and checks if current num is the same as prev, if so, skip. this effectively prevents reproducing the same outcomes from a sibling choice
        e.g. nums = [1,2,2]
        we could already have a [1,2] -> with 2 at i = 1, but we coudl aslo have a [1,2] -> with 2 at i = 2. by having that if statement, it blocks a sibling choice.
        [1,2,2] will still be not impacted and produced as normally as it passes the check since it allowws me to regualrly move onto the next start.

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
