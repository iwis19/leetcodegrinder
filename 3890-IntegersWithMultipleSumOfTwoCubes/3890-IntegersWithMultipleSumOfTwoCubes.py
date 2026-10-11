class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:

        """
        1. originally went for a 2 pointer approach of l = 0, r = 1000 (since cube root of 10^9), and looped in a helper function and paired pairs... got TLE.

        2. this sol just appends all possible cubes (smaller than n), and then found all possible combos of sums with each pair in O(n^2) (i,j) s.t. i < j, and then looped thru the freq map to check if greater than 2 or not

        lowkey a good sol now im looking bakc at this

        did this in new york as well. could optimize by instead of just looping through all possible b's after having a, i could just keep going until a3 + b3 > n.

        724ms runtime beats 18%
        """
        
        cubes = []

        x = 1
        while x**3 <= n:
            cubes.append(x**3)
            x += 1

        res = []
        count = {}

        for i in range(len(cubes)):
            for j in range(i, len(cubes)):
                sum = cubes[i] + cubes[j]
                if sum > n:
                    break
                count[sum] = count.get(sum, 0) + 1

        for i in sorted(count):
            if count[i] >= 2:
                res.append(i)

        return res
