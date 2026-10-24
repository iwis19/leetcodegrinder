class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        """
        dang i had no idea python could handle the leading zero so well w lang i love it

        + also optimized out of teh if statements that was goofy

        0 ms runtime beats 100%
        """

        def count_day(date: str):
            dates = date.split("-")
            month, day = int(dates[0]), int(dates[1])

            for i in range(month-1):
                day += days_in_month[i]

            return day

        a_leave, b_leave = count_day(leaveAlice), count_day(leaveBob)
        a_arrive, b_arrive = count_day(arriveAlice), count_day(arriveBob)

        """
        cases: 
            1. alice comes earlier and leaves later -> bobleave - bobarrive + 1
            2. alice comes earlier and leaves earlier -> aliceleave - bobarrive + 1
            3. alice comes later and leaves earlier -> aliceleave - alicearrive + 1
            4. alice comes later and leaves later -> bobleave - alicearrive + 1
        """

        ans = min(a_leave, b_leave) - max(a_arrive, b_arrive) + 1

        return max(0, ans)
            
