class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        
        """
        criteria:
        - a, b, c must be the max of the two triplets for each element.

        first look for all triplets containing the values in target at their specific locations
        we dont need to consider anything else because 1. if they give lower value, useless since we take max,
        2. if they give higher value, useless since we need target.

        we will do 3 searches for: index 0, index 1, index 2

        we only take triplets with the same element as index 0, other two elements are smaller than targe telements
        otherwise, we will not accept it.

        im a beast at the fucking ams lol omegalul kekw

        23 ms runtime beats 65%
        """

        trip1 = trip2 = trip3 = None

        for triplet in triplets:
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                trip1 = triplet
            if triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]:
                trip2 = triplet
            if triplet[2] == target[2] and triplet[0] <= target[0] and triplet[1] <= target[1]:
                trip3 = triplet

        if trip1 and trip2 and trip3:
            return True

        return False

