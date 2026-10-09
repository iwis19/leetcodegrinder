class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        """
        dp

        spent a lot of time debugging because im bugging and i set arr = arr = [0] and i did not notice that it wasnt referencing the correct array

        7 ms runtime beats 40%
        """
        
        min_prod, max_prod = [0], [0]
        res = max(nums)

        for n in nums:

            if n == 0:
                min_prod.append(0)
                max_prod.append(0)
                continue

            """
            max can only keep > 0 and min can only keep < 0
            """
            prev_min = 1 if min_prod[-1] == 0 else min_prod[-1]
            prev_max = 1 if max_prod[-1] == 0 else max_prod[-1]

            if n > 0:
                new_max = max(n * prev_max, n)
                new_min = min(n * prev_min, n)

            elif n < 0:
                new_max = max(n * prev_min, n)
                new_min = min(n * prev_max, n)

            max_prod.append(new_max)
            min_prod.append(new_min)

            res = max(res, new_max)

        return res



