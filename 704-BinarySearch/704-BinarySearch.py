class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """
        wow remembered

        0 ms runtime beats 100
        """

        l, r = 0, len(nums)-1

        # must be <= since number could be on when l == r
        while l <= r:

            mid = (l+r)//2
            num = nums[mid]

            if num == target:
                return mid
            if num > target:
                # nums[mid] did not equal to target so im gonna exclude mid as well, no point keeping
                r = mid-1
            if num < target:
                # same as one above
                l = mid+1

        return -1
        
