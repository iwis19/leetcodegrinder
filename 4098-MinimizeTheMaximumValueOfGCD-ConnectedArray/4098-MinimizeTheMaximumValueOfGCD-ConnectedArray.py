class Solution:
    def minimumMaxValue(self, n: int, index: int, value: int) -> int:

        """
        what the fuck was this

        in contest sol
        """

        if value == 1:
            return -1

        if not value%2:
            if value - 2 * index < 2:
                return -1
            return value + 2 * (n - index - 1)
        else:
            smallest_p = value
            d = 3

            while d**2 <= value:
                if value % d == 0:
                    smallest_p = d
                    break
                d += 2
            
            if index > 0 and value - smallest_p - 2 * (index - 1) < 2:
                return -1

            right = n - index - 1

            if not right:
                return value

            return value + smallest_p + 2 * (right - 1)

        return -1

            

        
