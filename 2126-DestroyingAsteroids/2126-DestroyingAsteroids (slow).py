class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        """
        solved in 2 mins but nlogn so checked out solutions, retrying now !

        70 ms beats 76%
        """
        
        asteroids.sort()

        for asteroid in asteroids:

            if mass >= asteroid:
                mass += asteroid
            else:
                return False

        return True
