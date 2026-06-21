class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        """
        wooooooooooo

        had some dum mistakes though like subtracting remaining with freq[i] instead of i

        but remembered what bucket srot was hahahahahha

        55 ms runtime beats 90%
        """
        
        freq = [0] * 100005

        for cost in costs:
            freq[cost] += 1

        remaining = coins
        res = 0

        for i in range(100005):
            if freq[i] == 0:
                continue

            if remaining - i < 0:
                break
            
            while remaining - i >= 0 and freq[i] != 0:
                res += 1
                freq[i] -= 1
                remaining -= i

        return res
