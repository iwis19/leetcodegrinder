class Solution:
    def sumAndMultiply(self, n: int) -> int:

        """
        basix

        confused as to why the tc is logn, but n is an integer and not a string, so n represents n value instead of array size.
        since integers are in base 10, amt of digits is logn + 1 and thats the tc for len, sum, for loop.

        .replace() would work like a charm in this problem. string.replace("0", "") gives a stripped string

        0 ms runtime beats 100%, logn tc
        """
        
        string = str(n)
        l = len(string)
        s = sum(int(string[i]) for i in range(l))
        arr = []

        for i in range(l):
            if string[i] != "0":
                arr.append(string[i])

        x = int("".join(arr)) if arr else 0

        return s * x
        

