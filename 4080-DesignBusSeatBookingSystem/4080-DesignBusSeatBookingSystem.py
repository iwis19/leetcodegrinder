class BusBooking:

    """
    fun impl problem, had initial TLE but fixed it by a constant time total_time and min_time solution

    also do not need a dict as i can just store the purchase value within the seats array

    weekly contest problem no runtime info
    """

    def __init__(self, n: int):
        self.seats = [ [0] * 4 for _ in range(n+1) ]  # A, B, C, D for n rows
        self.bookings = {}   # key -> seat name, val -> book time
        self.min_time = 0
        self.total_time = 0

    def toggle(self, seat: str) -> None:
        row, col = int(seat[1:]), ord(seat[:1]) - ord('A')
        curr_state = self.seats[row][col]
        if curr_state == 0:
            self.seats[row][col] = 1
            self.bookings[seat] = 1
            if (col == 0 and self.seats[row][col+1]) or (col == 3 and self.seats[row][col-1]):
                self.bookings[seat] += 2
            self.min_time += 1
            self.total_time += self.bookings[seat]
        else:
            self.seats[row][col] = 0
            self.min_time -= 1
            self.total_time -= self.bookings[seat]
            del self.bookings[seat]
        
    def getTotalTime(self) -> int:
        """
        doesnt have to be optimal
        """
        return self.total_time

    def getMinTime(self) -> int:
        """
        do all windows, then all middles
        """
        return self.min_time

# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()
