class Solution:
    def threeFibonacciSum(self, n: int) -> bool:

        """
        0 1 1 2 3 5 8 13

        e.g. term_n = term_n-1 + term_n-2
        therefore 3 consecutive terms = (term_n-1 + term_n-2)*2

        weekly contest problem no runtime info
        """

        fib = [0, 1]
        i = 2

        while fib[-1] <= n//2:
            if 2*(fib[i-2] + fib[i-1]) == n:
                return True
            fib.append(fib[i-2] + fib[i-1])
            i +=1
            
        return False

        
