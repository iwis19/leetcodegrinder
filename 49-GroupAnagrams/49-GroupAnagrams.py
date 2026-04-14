class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        1. had a little bit of trouble figuring out "".join(sorted(string)), since i originally tried using a list as a key... i didnt know sorted() would return a list
        2. other than that, it was great

        11 ms beats 85% - O(m*nlogn)
        """
        
        map = {}
        res = []

        for string in strs:

            s = "".join(sorted(string))
            if s not in map:
                map[s] = []
            map[s].append(string)

        for arr in map.values():
            res.append(arr)

        return res

