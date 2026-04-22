class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        """
        good problem

        1. i tend to question myself if there is a better option than brute force, and there usually always seems like there is, but for this one, it seems that
        brute force is better than a trie, miles better.
        2. i had duplicate answers and it was becauase i didnt properly read the question, but also because i didnt know how to do it either. seems that breaking the  
        loop for the current dictionaryword and moving onto the next solves this issue
        3. was thinking about checking diff == 3 in the middle of the loop and breaking, but didnt end up doing so to clean up my logic, but i shouldve added it
        afterwards again to improve efficiencdy significantly.

        10 ms runtime beatas 83% 
        """

        res = []
        
        for word in queries:

            for dictionaryword in dictionary:
                
                if len(word) != len(dictionaryword): continue
                diff = 0

                for i in range(len(word)):
                    if word[i] != dictionaryword[i]:
                        diff += 1
                    if diff == 3:
                        break

                if diff <= 2:
                    res.append(word)
                    break

        return res

                


                

