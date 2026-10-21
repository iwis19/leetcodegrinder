class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        
        """
        i do greedy

        ok i knew everything besides how to start this loop i had like 0 clue even though it was so simple

        i was also bugging thinking that when groupSize = 1 and len(hand) = 10**4, this would be very bad, but
        len(hand) * groupSize is a fine case.

        esp when i skip on amt = 0, this is as reduced as it gets

        31 ms runtime beats 64%, the main loop does at most O(n) loops but sort brings it to O(nlogn)
        """

        n = len(hand)

        if n%groupSize:
            return False

        hand.sort()
        freqs = Counter(hand)

        for card, amt in freqs.items():
            if amt == 0:
                continue
            
            for i in range(card, card+groupSize):
                freqs[i] -= amt
                if freqs[i] < 0:
                    return False

        return True



