class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        """
        actually washed wtf i had a hard time thinking of a good solution and had to look at solutions?????

        was okay on implementation though i think...

        47 ms runtime beats 45% will do b-search now
        """
        
        temp = sorted(arr)
        ranks = {}
        rank = 1

        for num in temp:
            if num not in ranks:
                ranks[num] = rank
                rank += 1

        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]

        return arr
