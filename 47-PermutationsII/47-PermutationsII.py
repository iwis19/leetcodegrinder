class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        """
        did something similart in combination sum II, but wanted to figure out how everyone else did it

        obv could setup a visited set to check if what im appending exists in the set alr

        for future reference, when i have to do more "unique" related problems like this, i can keep the same structure, but add a manual check (way faster than using visited set like before), and design the logic by myself.

        """

        nums.sort()    # first must sort for the nums[i] == nums[i-1] to fnction
        res = []
        n = len(nums)
        
        def dfs(prev_set, prev_arr):

            if len(prev_arr) == n:
                res.append(prev_arr[:])
                return

            for i in range(n):

                if i in prev_set:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and i - 1 not in prev_set:
                    continue
                    
                prev_set.add(i)
                prev_arr.append(nums[i])

                dfs(prev_set, prev_arr)

                prev_set.discard(i)
                prev_arr.pop()

        dfs(set(), [])

        return res
