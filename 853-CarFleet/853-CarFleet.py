class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        """
        - car A can only get slowed down by the car ahead of it, not behind it
            - catches up to infront --> car A speed > car infront speed --> fleet speed = infront
            - behind catches up --> car A speed < car behind speed --> fleet speed = car A

        needed lots of help on this to get the monotonic stack idea, but also spent a lot of time on this so hopefully sticks w me

        also learned what zip does so pretty cool

        164 ms runtime beats 57%
        """

        # zip pos + speed then sort then in reverse (closest to target -> farthest)

        secs_from_target = []
        cars = len(position)

        for i in range(cars):
            secs = (target - position[i])/speed[i]
            secs_from_target.append((position[i], secs))

        secs_from_target.sort(key=lambda x: -x[0])

        stack = [secs_from_target[0][1]]

        for i in range(1, cars):
            if secs_from_target[i][1] > stack[-1]:
                stack.append(secs_from_target[i][1])

        return len(stack)
