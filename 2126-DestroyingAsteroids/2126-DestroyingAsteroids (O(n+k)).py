class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        """
        counting sort.

        this was a slower runtime and it bamboozled me. but just like how string splicing is very efficient for palindromes 
        as its written in C, sort() is also very efficient for N values under 10^5. so i should remember this.
        even tho n+k looks good and it should be good, nlogn for smaller N and optimized C is way faster.

        116 ms beats 15%
        """
        
        largest = max(asteroids)
        count = [0] * (largest+1)

        for asteroid in asteroids:
            count[asteroid] += 1

        for i in range(len(count)):

            if count[i] == 0:
                continue

            if mass >= i:
                mass += count[i] * i
            else:
                return False

        return True
