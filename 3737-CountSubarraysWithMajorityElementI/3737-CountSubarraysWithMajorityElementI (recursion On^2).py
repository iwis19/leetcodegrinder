class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:

        """
        bro ive been doing way too much recursion 💀💀💀💀💀💀💀

        doing recursion for ANYTHING now

        4070 ms runtime beats 5%, O(n^2) solution because prefix sum is too hard, will def do soon. will mark this as come back soon asw to do in prefix su m after i learn
        """
        
        res = 0
        n = len(nums)

        """
        [1,2,2,3]

        [0..2]
        [1..1], [1..2], [1..3]
        [2..2]

        do not do pure math using amt of target # in nums
        """

        #
        def solve(start_index, prev_arr_len, amt_target):

            nonlocal res
            
            if amt_target > prev_arr_len // 2:
                res += 1

            if start_index == n:
                return

            solve(start_index + 1, prev_arr_len + 1, amt_target + 1 if nums[start_index] == target else amt_target)

        for i in range(n):
            solve(i, 0, 0)

        return res
