class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        """
        brute force not inplace bad space complexity probably

        29 ms runtime beats 65% although idk how the exact same code is also 7 ms in the code samples
        """
        
        less, equal, more = [], [], []

        for num in nums:

            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                more.append(num)

        return less + equal + more
