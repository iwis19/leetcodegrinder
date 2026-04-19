class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        """
        idk i think ireally needed help on this one maybe im jus tbad

        if condition works, we increment j to find possible bigger dist
        if condition fails, we increment i to make condition work by decreasing nums1[i]
        - however, we make j match with i when i is greater than j since we must force it to make the window legal

        36 ms runtime beats 70
        """
        

        i, j = 0, 0
        res = 0

        while i < len(nums1) and j < len(nums2):
            
            # if it meets condition, we want to increment j to find MAX distance until it fails
            if nums1[i] <= nums2[j] and i <= j:
                res = max(res, j-i)
                j += 1
            # once it stops working, we want to increment i to get a smaller nums1[i] and check if i > j (which we dont want), so we move j = i as well. (essentailly decreasing both if i > j)
            else:
                i += 1
                if i > j:
                    j = i

        return res
