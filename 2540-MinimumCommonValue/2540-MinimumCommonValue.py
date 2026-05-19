class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:


        """
        W APPROACH W TIME COMPLEXITY W TWO POINTER

        1 ms runtime beats 99.26% O(n+m)
        """
        
        n1, n2 = len(nums1), len(nums2)

        j = 0

        for i in range(n1):

            while j < n2 and nums2[j] < nums1[i]:
                j += 1

            if j < n2 and nums1[i] == nums2[j]:
                return nums1[i]
            
        return -1
