class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        """
        essentially, remove all trailing 0s

        since an integer cant start with a 0 digit (unless 0 base case), that means there wont be any leading 0s

        brains clogged after so long i thought to convert num to a string then splice last char but i couldve just done a modulo the whole time
        
        0 ms runtime beats 100%
        """

        if num == 0:
            return True

        return num % 10 != 0

