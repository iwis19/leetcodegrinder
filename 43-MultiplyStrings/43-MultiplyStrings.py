class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        """
        lowkey i read hte question and i had some questions abt the bigint library or converting inputs directly so i took a look at sol but i coded sol myself

        4 ms runtime beats 62%
        """
        
        def decode(string: str) -> int:

            ans = 0
            for i in range(len(string)):
                ans = ans*10 + (ord(string[i])-48)

            return ans

        def encode(num: int) -> str:

            if num == 0:
                return "0"
            ans = ""
            while num > 0:
                digit = num % 10
                num //= 10
                ans = chr(digit+48) + ans
            
            return ans

        return encode(decode(num1)*decode(num2))
