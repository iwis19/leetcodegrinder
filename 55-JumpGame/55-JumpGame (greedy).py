class Solution:
    def canJump(self, nums: list[int]) -> bool:
        
        """
        trying the greedy algo i saw on the most efficient sols

        it just keeps moving forward by 1 in a greedy approach:
        - if i can move to this index without moves < 0, then i continue
        - if this current step i reached rn gives me more steps than i hold, then i recharge w it by swapping

        18 ms runtime beats 65%
        """

        moves = 0
        n = len(nums)

        for i in range(n):
            if moves < 0:
                return False

            if nums[i] > moves:
                moves = nums[i]

            moves -= 1

        return True
