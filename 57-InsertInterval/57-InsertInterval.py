class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        """
        man fuck what the hell am i doing

        gotta do max(prev_e, curr_e)

        0 ms runtime beats 100%
        """

        intervals.append(newInterval)

        intervals.sort()

        res = [intervals[0]]


        """
        partially overlap, entirely overlap, nothing

        partial: if next_s < curr_e
        """

        for i in range(1, len(intervals)):

            curr_s = intervals[i][0]
            curr_e = intervals[i][1]

            prev_s = res[-1][0]
            prev_e = res[-1][1]

            if curr_s <= prev_e:
                res[-1][1] = max(prev_e, curr_e)
            else:
                res.append([curr_s, curr_e])

        return res



            


        
