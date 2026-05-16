class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums)-1

        while l < r:

            m = (l+r) // 2

            # for test cases like [10,1,10,10,10], the statement at ln22 would fail since it would think the leftside is sorted when in reality it is not.
            # this helps us find the 1 that could be hidden anywhere in the program
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
                # we move both ptrs since left and right are the same values, so even when we move it, the abs min is preserved

            # both sides are sorted
            elif nums[l] <= nums[m] and nums[m] <= nums[r]:
                return nums[l]

            # only left is sorted, min is in the right half
            elif nums[l] <= nums[m]:
                l = m+1

            # only right is sorted, min is in the left
            else:
                r = m

        return nums[l]
