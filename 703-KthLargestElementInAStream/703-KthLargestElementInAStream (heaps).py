from heapq import heappush, heappop, heapify, nlargest

class KthLargest:

    """
    dang if it wasnt for the fact that i knew this problem was heaps i wouldnt have used this. 
    
    need to get better at heaps tbh, but other ppl r also agreeing its medium difficulty interms of non brute force w heaps

    30 ms runtime beats beats 50%
    """

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.stream = nlargest(k, nums)
        heapify(self.stream)

    def add(self, val: int) -> int:

        """
        since numbers are NEVER removed, we really only care when a number > current kth largest element is placed into
        the stream

        realistically we only need a minheapq with the top k elements. 

        i check if the new value is greater than curr stream[0], if so, i push it to heap and pop smth, then return 
        stream[0]
        """

        if len(self.stream) < self.k or val > self.stream[0]:
            heappush(self.stream, val)
            if len(self.stream) > self.k:
                heappop(self.stream)
        
        return self.stream[0]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
