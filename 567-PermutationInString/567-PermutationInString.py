class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        """
        original: 
        sliding window

        keep a Counter of s1, and i think we can do a O(n) sol?

        left pointer begins on 0, and we splice (maybe not as its not efficient) [l:l+n], where n is len(s1)

        i think the trick is to check if curr left pointer is in counter, if not, skip

        and i think it might also be especially useful to keep track of prev characters that we just went through

        afterwards:
        good basic thinkings for interviews, but still need more practice on sliding windows:
        - index management from lots of practice
        - idea. i had a good general idea, etc, but it was just yap if i miss the biggest part of keeping a realtime freq arr as i move thru. i was just 
        still thinking of splicing area + slamming ccounter + compare

        13 ms runtime beats 84%
        """

        n1, n2 = len(s1), len(s2)

        if n2 < n1:
            return False

        c1, c2 = [0]*26, [0]*26

        for i in range(n1):
            c1[ord(s1[i]) - ord('a')] += 1

        for i in range(n2):
            if c1 == c2:
                return True
            c2[ord(s2[i]) - ord('a')] += 1
            if i < n1: 
                continue
            c2[ord(s2[i-n1]) - ord('a')] -= 1

        return c1 == c2

