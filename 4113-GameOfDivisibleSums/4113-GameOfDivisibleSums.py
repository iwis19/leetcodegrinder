class Solution:
    def maxDifference(self, nums: list[int]) -> int:

        """
        alice goes first

        takes either 1 or 2 leftmost elements

        sum of the elements taken determines:
        - if sum%3 == 0: other player plays
        - else: same player plays

        score = sum(all elements taken by a player)

        both players play optimally until elemenets are taken

        return alice - bob
        """

        """
        if 1 or 2 both are divisble, take 2, play again
        if 1 and 2 both arent divisble, take 2, play again
        if 1 is divisible and 2 isnt, take 2, play again
        if 1 isnt divisble and 2 is, take 1. -> because (a+b)%3 != 0 if a%3 != 0 and b%3 == 0

        but maybe dp...? AND HOWS EVERYONE SCORING 200 MS WTF
        """

        n = len(nums)

        @cache
        def dp(i):

            if i == n:
                return 0

            best = -math.inf

            for k in (1,2):
                if i+k > n:
                    continue

                total = sum(nums[i:i+k])

                if total % 3 == 0:
                    diff = total - dp(i+k)
                else:
                    diff = total + dp(i+k)

                best = max(diff, best)

            return best

        return dp(0)
                
