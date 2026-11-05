class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        
        """
        just gonna have to binary search closest number

        geeg ferkin HORRENDOUS WTF AM I DOING

        12 ms runtime beats 67%
        """

        n = len(arr2)
        arr2.sort()

        def search_closest(target):
            l, r = 0, n-1
            m = (l+r)//2

            while l <= r:
                m = (l+r) // 2
                if arr2[m] == target:
                    return m

                # too big
                if target < arr2[m]:
                    r = m-1
                # rightside is closer
                else:
                    l = m+1

            return m

        ctr = 0

        for num in arr1:
            closest = search_closest(num)
            one = two = three = abs(num - arr2[closest])
            if closest + 1 < n:
                two = abs(num - arr2[closest+1])
            if closest - 1 >= 0:
                three = abs(num - arr2[closest-1])

            if min(one, two, three) > d:
                ctr += 1

        return ctr
