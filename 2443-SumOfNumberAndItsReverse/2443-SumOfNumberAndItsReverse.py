class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:

        def reverse(num: int) -> int:
            return int(str(num)[::-1])

        # technically only have to check half of the range since 14 + 41 is the same, even tho i shortcircuit it after i find an answer, we have to consider worst case scenario, where the answer is false!
        for i in range(num//2, num+1): 
            if i + reverse(i) == num:
                return True

        return False
