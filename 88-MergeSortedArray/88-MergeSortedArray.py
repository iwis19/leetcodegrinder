class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """


        """
        i had a pretty good general idea of eveyrthing, from out of bounds cases to two pointer, i just did not think about starting from the BACK
        of the array, and i sttuck with going with the start so ineeded to take a look at the solutions, but no code, just explanation for starting
        from the back

        sometimes i need to tghink the other way more

        0 ms runtime beats 100%
        """

        i, j = m-1, n-1

        k = m+n-1

        for curr in range(k, -1, -1):

            num1 = nums1[i] if i >= 0 else -math.inf

            num2 = nums2[j] if j >= 0 else -math.inf

            if num1 >= num2:
                nums1[curr] = num1
                i -= 1
            else:
                nums1[curr] = num2
                j -= 1
            
