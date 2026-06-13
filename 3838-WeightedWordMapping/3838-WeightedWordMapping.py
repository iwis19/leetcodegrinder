class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:

        """
        took like 5-10 mins to write the solution? thinking back the time it took was okay but i got stuck on thinking abt how to get the 
        reverse letter

        looked at some solutions afterwards to fully optimize my runtime
        - originally had a second loop + another arr to calculate reverse letter and append it
        - realized could just combine them straight up instead of 2 loops and arrays -> optimized a bit
        - used numbers instead of relying on ord('z') and ord('a') -> optimized speed a lot

        0 ms runtime beats 100% + good memory use
        """
        
        res = []

        for word in words:
            tot = 0
            for char in word:
                tot += weights[ord(char) - 97]
            res.append(chr(122 - tot%26))

        return "".join(res)
