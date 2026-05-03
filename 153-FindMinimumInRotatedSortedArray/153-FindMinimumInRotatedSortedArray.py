class Solution:
    def findMin(self, nums: List[int]) -> int:

        """
        SO happy i remmebered the idea (1st ocmment)

        intu itively debugged but need to understand the idea more but regardless im actually happy i remembered and learned things



        0 ms runtime beats 100
        """
        
        # the idea is that half of the array is always going to be sorted

        l, r = 0, len(nums)-1

        while l <= r:

            m = (l+r)//2

            # left is sorted, right is sorted, both are sorted

            # both sorted, l is SMALLEST
            if nums[l] <= nums[m] and nums[m] <= nums[r]:
                return nums[l]

            # left is sorted, then r has SMALLEST
            if nums[l] <= nums[m]:
                l = m + 1      
            # i keep this as l = m+1 because m cannot be the min when left is sorted, e.g. [3,4,5,1,2] -> [3,4,5] [5,1,2], so the big drop ALWAYS
            # happens AFTER m, or else left is NOT sorted.


            # right is sorted, then l has SMALLEST
            else:
                r = m  
            # i keep this as r = m and not r = m-1 because m could be the min, since e.g. [3,1,2] -> [3,1] [1,2], so m could potentially be the ans
            # as it could be the drop

        return None
