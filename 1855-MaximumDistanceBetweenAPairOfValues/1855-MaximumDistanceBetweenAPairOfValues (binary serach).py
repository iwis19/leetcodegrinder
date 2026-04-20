class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        """
        binary search try, went pretty good

        honestly ihave no idea why people chose/leetcode put tag as binary search, since this efficiency is so trash and worse than 2ptr O(nlogn)
        """

        res = 0
        
        for i, num in enumerate(nums1):

            l, r = i, len(nums2)-1

            while l <= r:

                mid = (l+r)//2

                if nums2[mid] >= num:
                    res = max(res, mid-i)
                    l = mid + 1

                # since nums2 is decreasing, when nums2[mid] < num, we have to make r = mid-1 (moving towards left half of arr)
                elif nums2[mid] < num:
                    r = mid-1

        return res
                    
