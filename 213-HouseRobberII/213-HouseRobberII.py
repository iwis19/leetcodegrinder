class Solution:
    def rob(self, nums: list[int]) -> int:
        
        """
        cannot take 1 step and alert the police

        crazy idea but i work backwards

        i think nums[i] += max(nums[i+1:]), but specifically at i = 0, it cannot reach last house

        and then return nums[0]

        [1,2,3,1] -> original

        [1,2,3,1] -> 3

        [1,2,3,1] -> 2 *3+None = 3

        [1,3,3,1] -> 1 *2+nums[3] = 3

        [4,3,3,1] -> 0 *explicitly ignored n-1th index, only [2, inf), != n-1

        this fails sometimes because if n = odd, and i do 0, 2, 4, it contains both first and last index...

        took a LONG LONG LONG FUCKING TIME to solve this to deal with indices, also needed a design hint:
        - since i cant have 0 and n-1 th house touch, i can just do two solves where i go to 0->n-2 inclusive and 1->n-1 inclusive.
        - this way, its impossible it include both endpoints and remoevs the need of doing brute checks and failing.

        0 ms runtime beats 100%
        """

        n = len(nums)

        if n < 4:
            return max(nums)

        def solve(nums):
            maximum = 0
            maximum_1 = 0
            n = len(nums)

            for i in range(n-1, -1, -1):
                if i <= n-2:
                    maximum = max(maximum, nums[i+1])
                nums[i] += maximum_1
                maximum_1 = maximum

            return max(nums)

        return max(solve(nums[1:]), solve(nums[:-1]))





