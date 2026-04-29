class Solution:
    def countAndSay(self, n: int) -> str:

        """
        this is the recursion method and im highkey kind of stupid so i had to get a quick refresher on how 
        recursions looked but i got it on my own

        however for rle... i initially thought about using string[i] == string[i+1], but its easier to deal 
        with overflow (leftovers) at the end after my loop, so i shouldve used string[i] == string[i-1] from 
        the start, at least now i know how it works

        7 ms runtime beats 77% 
        """

        def rle(string: str) -> int:
            count = 1
            res = ""

            for i in range(1, len(string)):
                if string[i] != string[i-1]:
                    res += f"{count}{string[i-1]}"
                    count = 1

                elif string[i] == string[i-1]:
                    count += 1
                
            res += f"{count}{string[-1]}"
            
            return res


        if n == 1:
            return "1"
        return rle(self.countAndSay(n-1))
    
        

        
