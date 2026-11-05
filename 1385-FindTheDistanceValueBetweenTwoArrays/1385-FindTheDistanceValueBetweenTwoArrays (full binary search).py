class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        
        """
        just gonna have to binary search closest number -> know that binary search pretty much also gives away the closest num index by just choosing to move left or right pointers based on size.

        geeg ferkin HORRENDOUS WTF AM I DOING

        15 ms runtime beats 63%
        """

        n = len(arr2)
        arr2.sort()

        def search_closest(target):
            l, r = 0, n-1
            m = (l+r)//2

            while l <= r:
                m = (l+r) // 2
                if arr2[m] == target:
                    return 0

                # too big
                if target < arr2[m]:
                    r = m-1
                # rightside is closer
                else:
                    l = m+1

            closest = math.inf
            if l < n:
                closest = min(closest, abs(target - arr2[l]))
            if r >= 0:
                closest = min(closest, abs(target - arr2[r]))

            return closest

        ctr = 0

        for num in arr1:
            if search_closest(num) > d:
                ctr += 1

        return ctr
