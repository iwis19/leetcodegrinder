class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        """
        131 ms runtime beats 58% already optimized tho
        """

        # USING int(str(num)[::-1]) is WAY MORE MORE MORE efficient, actually way more efficient as it is coded in C under the hood
        # def reverse(num: int) -> int:

        #     res = 0
        #     while num > 0:
        #         digit = num % 10
        #         num //= 10
        #         res = res*10 + digit

        #     return res

        n = len(nums)
        seen = set()

        for i in range(n):
            seen.add(nums[i])
            seen.add(int(str(nums[i])[::-1]))

        return len(seen)
