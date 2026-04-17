class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:

        """
        yay optimal solution O(N*D)

        1. needed a bit of help coding helper function reverse but thats because i wanted an optimal way of writing to memorize/fully understand
        2. needd to read question a bit more carefully, esp that i checked if nums[i] == reverse(nums[j]) instead of reverse(nums[i]) == nums[j]

        336 ms runtime beats 24 but i think python just butt
        """
        
        # write a helper function to reverse

        # loop thru while mapping all values

        min_dist = math.inf
        map = {}

        def reverse(num: int) -> int:
            
            res = 0
            pow = 0
            while num > 0:
                digit = num % 10
                res = res * 10 + digit
                num //= 10

            return res

        for i, num in enumerate(nums):
            if num in map:
                min_dist = min(min_dist, i - map[num])
            map[reverse(num)] = i

        return -1 if min_dist == math.inf else min_dist
