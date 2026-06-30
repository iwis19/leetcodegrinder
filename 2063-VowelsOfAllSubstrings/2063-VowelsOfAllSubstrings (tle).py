class Solution:
    

    def countVowels(self, word: str) -> int:

        """
        tle, even tho this was linked to be related to the daily, the actual sol lowkey had nothing to do w each other

        tle didnt get a sol
        """
        
        l = r = 0
        n = len(word)
        res = 0
        VOWELS = {'a', 'e', 'i', 'o', 'u'}

        for i in range(n):
            
            curr = 0
            while i < n:
                if word[i] in VOWELS:
                    curr += 1
                res += curr
                i += 1

        return res
                
