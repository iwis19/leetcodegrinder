class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        """
        spent some time thinking and had 2 general ideas: O(n^2) and sort of thought about teh stack, but didnt really see how i could implement it so i had to take a look at solution

        recoded a solid solution

        107 ms runtime beats 40, but optimized O(n)
        """
        
        l = len(temperatures)
        res = [0]*l
        stack = []

        for i in range(l):
            if not stack:
                stack.append(i)
                continue
            while stack and temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop(-1)
            stack.append(i)

        return res
