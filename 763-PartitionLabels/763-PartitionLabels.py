class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        """
        yessssss dubs

        2 ms runtime beats 89%
        """
        
        seen = [ [-1, -1] for i in range(26) ]

        used = 0

        for i, char in enumerate(s):
            index = ord(char)-ord('a')
            if seen[index][0] == -1:
                seen[index][0] = i
                used += 1
            seen[index][1] = i

        seen.sort()
        seen = seen[26-used:]

        """
        0,8 9,15 16,23 just combine intervals now
        """

        combined = [seen[0]]

        for i in range(1, len(seen)):
            if seen[i][1] <= combined[-1][1]:
                continue
            if seen[i][0] <= combined[-1][1]:
                combined[-1][1] = seen[i][1]
            else:
                combined.append(seen[i])

        return [ end-start+1 for start,end in combined ]


        

        

            
            
