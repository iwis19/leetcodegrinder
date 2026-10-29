class KthLargest:

    """
    monkey garbage solution for fun now doing heaps
    """

    def __init__(self, k: int, nums: list[int]):
        self.all = nums
        self.k = k

    def add(self, val: int) -> int:
        self.all.append(val)
        self.all.sort()
        return self.all[-1 - self.k + 1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
