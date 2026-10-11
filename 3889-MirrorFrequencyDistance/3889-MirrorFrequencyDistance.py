class Solution:
    def mirrorFrequency(self, s: str) -> int:

        """
        hoolee sheet bruh this is from like 2026 newyork trip

        960 ms runtime beats 23%
        """

        #two arrs -> one for digits, one for alphabets

        res = 0

        alphabets = [0]*26
        l_a = 26
        digits = [0]*10
        l_d = 10

        for char in s:

            if ord('a') <= ord(char) <= ord('z'):
                alphabets[ord(char)-ord('a')] += 1
            else:
                digits[ord(char) - ord('0')] += 1

        for i in range(l_a//2):
            res += abs(alphabets[i] - alphabets[l_a-i-1])
        for i in range(l_d//2):
            res += abs(digits[i] - digits[l_d-i-1])

        return res
        
