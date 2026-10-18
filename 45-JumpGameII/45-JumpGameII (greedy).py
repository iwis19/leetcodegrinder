class Solution:
    def jump(self, nums: list[int]) -> int:
        
        """
        idt i can use greedy here as i may skip over very big steps 

        acc greedy i can by scanning over i -> i+nums[i] to find the biggest step and move on?

        took way too long and realized im retarded

        5 ms runtime beats 63%
        """

        n = len(nums)

        if n == 1:
            return 0

        res = 0
        i = 0

        while i < n-1:
            max_reach_i = i
            max_reach = i + nums[i]

            if max_reach >= n-1:
                return res + 1

            for j in range(i+1, i+1+nums[i]):  # can go out of n, also want to include i+nums[i] (reach)
                if j < n and j + nums[j] >= max_reach:
                    max_reach = j + nums[j]
                    max_reach_i = j
            res += 1
            if i == max_reach_i:
                break
            i = max_reach_i

        return res

