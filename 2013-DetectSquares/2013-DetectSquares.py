class DetectSquares:

    """
    needed a little bit of intuition help, but i remembered hte diagonal rule from another prev question which was pretty cool

    90 ms runtime beats 65%, will be back
    """

    def __init__(self):
        self.vertices = Counter()  # point freq checker
        
    def add(self, point: list[int]) -> None:
        self.vertices[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        
        # in a square, diag has slope 1 or -1
        # either x-y -> e.g. 11,10 and 3,2 -> gives 1
        # or x+y -> e.g. 3,10 and 11,2 -> gives 13

        x1,y1 = point
        diag_pos = x1-y1
        diag_neg = x1+y1

        count = 0

        for (x3,y3), freq in self.vertices.items():

            # must not be same point
            if x3 == x1 and y3 == y1:
                continue

            # p3 doesnt make a perfect diagonal with p1, skip
            if x3+y3 != diag_neg and x3-y3 != diag_pos:
                continue

            count += freq * self.vertices[(x1, y3)] * self.vertices[(x3, y1)]

        return count



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
