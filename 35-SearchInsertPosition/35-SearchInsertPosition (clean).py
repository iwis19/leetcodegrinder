class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        """
        this is the clean solution version

        1. i originally forced myself to think in individual gaps and edge case handling, which honestly was a linear for loop solution disguised in a binary loop
        2. the idea for binary search oftentimes is to abuse the l and r values

        e.g. nums = [1,3,5,6] target = 4
        step1 : l, mid, r = 0,1,3, nums[1] < 3, so l = 2
        step2: l, mid, r = 2,2,3, nums[2] > 3, so r = 1

        now that l > r, the loop stops running and we return 2, which is where its supposed to be inserted.

        we essentially just keep moving either pointers until the left one is at where it is supposed to be, and then the loop will eventually break where we can just return it instead of specifically checking gaps and handling edge.


        0 ms runtime beats 100
        """
        
        # probably a binary search variation

        l,r = 0, len(nums)-1

        while l <= r:

            mid = (l+r)//2
            
            if target == nums[mid]:
                return mid

            if target > nums[mid]: l = mid+1
            elif target < nums[mid]: r = mid-1

        return l
