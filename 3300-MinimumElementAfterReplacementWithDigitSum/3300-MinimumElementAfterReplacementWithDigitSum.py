class Solution:
    def minElement(self, nums: List[int]) -> int:

        """
        very simple one for today

        2 ms runtime beats 87% but optimal time complexity and style and i also remembered that methods are less efficient htan just straight up implemented if used oinly once so i took it out tooptimize hohoho
        """

        res = math.inf

        for num in nums:
            sum = 0
            while num > 0:
                sum += num % 10
                num //= 10
            
            res = min(res, sum)

        return res
