class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        woo hoo debugged on vscode myself

        not really junk code, but i couldve def used slicing.

        6 ms runtime beats 61%
        """
        
        n = len(nums)
        k %= n # in case k > n

        """
        intuition: 
        make a separate arr to temporarily store the last k values in an arr
        move everything forward by k
        put separate arr values in order into the start of nums
        """
        
        if k > 0:
            temp = [0] * k
            for i in range(n-1, n-k-1, -1):
                temp[i - n + k] = nums[i]

            for i in range(n-k-1, -1, -1):
                nums[i+k] = nums[i]
                
            for i in range(k):
                nums[i] = temp[i]
