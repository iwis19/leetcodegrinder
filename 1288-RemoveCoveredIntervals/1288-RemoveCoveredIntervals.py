class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        """
        best debugging experience ive ever had and most brain power ever used to fix this but i did it woohohooo

        3 ms runtime beats 77%, optimal tc nlogn tho
        """
        
        """
        [1,4] [2,8] [3,6]

        [4218,57729], [9103,31953] (skipped), [20993,92876], [33272,92693] (skipped), [43332,89722] (skipped), [52631,65356] (skipped), 
        [54859,69855] (skipped), [59890,65654] (skipped), [66672,75156] (skipped), [92950,95965]

        [1,4], [2,8], [2,9], [3,6], [3,7]

        [1,2], [1,4], [3,4]


        the problem is: 
        
        i dont add 1 to results var when a new interval (that is valid) has same start as a prev interval (that wasnt valid)

        so if a interval wasn't valid, im gonna mark the start to somethign diff

        so when curr interval has the same start as prev interval, then the prev interval was untouched therefore it was valid and already accounted for. so i skip it without adding 1 to res and i increase the max_e regardless.


        what i need to do is:

        mark invalid intervals w a diff start as a indicator

        only add to res when the prev_s and curr_s are different
        """

        res = 0
        intervals.sort()
        max_e = -1

        for i in range(len(intervals)):
            curr_s, curr_e = intervals[i][0], intervals[i][1]
            if curr_e > max_e:
                max_e = curr_e
                prev_s = intervals[i-1][0]
                if prev_s != curr_s or i == 0: 
                    res += 1
            else:
                intervals[i][0] = -1

        return res
