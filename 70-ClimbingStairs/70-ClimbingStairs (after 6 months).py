class Solution:
    def climbStairs(self, n: int) -> int:
        
        """
        bottom up dp

        have arr, each i means how many ways allow me to get here

        this is essentially the fib sequence because if there is 1 way to get to 1, and 2 ways to get to 2, then i can do 1+2 and 2+1 so 3 ways to get to 3.
        """

        arr = [0, 1, 2]

        if n < 3:
            return arr[n]

        for i in range(2, n):
            arr.append(arr[i] + arr[i-1])

        return arr[n]

