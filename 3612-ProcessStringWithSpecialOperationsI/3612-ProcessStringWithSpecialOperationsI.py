class Solution:
    def processStr(self, s: str) -> str:

        """
        this was a good refresher on some of the string and array method slike

        isalpha() -> checks if its a letter a-z
        extend() -> adds the content to the back of an array
        reversed() -> returns a list reversed
        reverse() -> edits it inplace
        splicing in general, honestly okay with this one but i just didnt use it since i begun with arrays

        43 ms beats 40% with arrays, 7 ms beats 72% with string
        """
        
        res = ""

        for char in s:

            if char == "*":
                res = res[:-1]
            
            elif char == "#":
                res += res
            
            elif char == "%":
                res = res[::-1]

            else:
                res += char

        return res
