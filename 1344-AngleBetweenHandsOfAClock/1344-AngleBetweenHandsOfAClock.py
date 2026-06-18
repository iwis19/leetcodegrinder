class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        one_hour_angle = 30
        one_minute_in_hour_angle = 0.5
        one_minute_angle = 6

        hour_angle = (hour % 12 * one_hour_angle) + (minutes * one_minute_in_hour_angle)
        minute_angle = minutes * one_minute_angle

        angle = abs(hour_angle - minute_angle)

        return angle if angle <= 180 else 360 - angle
