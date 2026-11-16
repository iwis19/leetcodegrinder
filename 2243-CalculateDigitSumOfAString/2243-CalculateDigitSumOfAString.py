class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        # since splicing is very safe

        """
        i am retarded for accidentally converting 111 into 111 by doing total = total*10 like the du mbass i am

        1 ms runtime beats 25% but def is optimal if i just take out the func
        """

        def combine(s):
            total = 0
            for digit in s:
                total += int(digit)
            return str(total)

        while len(s) > k:
            combined = []
            for i in range(0, len(s), k):
                combined.append(combine(s[i:i+k]))
            s = "".join(combined)

        return s
