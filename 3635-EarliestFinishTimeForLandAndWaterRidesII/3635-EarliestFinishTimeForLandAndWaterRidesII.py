class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        """
        same code but diff constraints. 1000 -> 10^5

        i think this time complexity is more than fine, just can be optimizedd to uses comparison ops instead of min max function calls

        136 ms runtime beats 40%
        """
        
        m, n = len(waterDuration), len(landDuration)

        min_water_end = min(waterStartTime[i] + waterDuration[i] for i in range(m))
        min_land_end = min(landStartTime[i] + landDuration[i] for i in range(n))
        
        res = math.inf

        # land first
        for i in range(m):
            res = min(res, max(waterStartTime[i], min_land_end) + waterDuration[i])

        # water first
        for i in range(n):
            res = min(res, max(landStartTime[i], min_water_end) + landDuration[i])

        return res
