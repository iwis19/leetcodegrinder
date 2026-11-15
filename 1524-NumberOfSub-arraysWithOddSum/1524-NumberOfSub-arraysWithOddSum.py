class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:

        """
        cool prefix sum use. needed help on this but its fine will come back to it

        139 ms runtime beats 15%. optimal sol uses a math shortcut which i will NOT and can NOT understand
        """
        
        prefix = [0]
        n = len(arr)
        MOD = 10**9 + 7

        for num in arr:
            prefix.append(prefix[-1] + num)

        # maybe i just keep a count of both even and odd that ive seen and then whenever i come across
        # a new sum, i see if thats even or odd, and then i take the amt of nums thats the opposite basicaly

        # note: 0 counts as even
        even, odd = 1, 0
        res = 0

        for i in range(1, n+1):
            if prefix[i]%2:  # odd
                res += even
            else:
                res += odd

            res %= MOD

            if prefix[i]%2:
                odd += 1
            else:
                even += 1

        return res

