class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        """
        IM ZE BEST

        originally cut down left and right when left was just equal to right, but it could accidentally discard usef ul information since it could acciidentally delete the number want to find. now, we updated it to that oinly if it equals to nums[m] would we keep on moving left and right

        0 ms runtime beats 100%
        """
        
        # binary search

        # one side is always going to be sorted

        l,r = 0, len(nums)-1

        while l <= r:

            m = (l+r)//2

            # straight up equals
            if nums[m] == target:
                return True

            # move both sides (added a check for left on the if statement above)
            while l <= r and nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
            
            # otherwise, we have 2 cases: left side contains target OR right side contains target

            if l <= r:
                # 1: left contains: goes into 2 -> sorted, unsorted
                if nums[l] <= nums[m]:
                    if nums[l] <= target <= nums[m]:
                        r = m-1
                    else:
                        l = m+1
                
                # 2: right contains: goes into 2 -> sorted, unsorted
                else:
                    if nums[m] <= target <= nums[r]:
                        l = m+1
                    else:
                        r = m-1
            
        return False
