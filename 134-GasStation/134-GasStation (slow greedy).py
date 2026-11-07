class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        
        """
        i think teh twist to this problem is that each step uses up some cost x,
        and if the cost isnt enough then prev points all cant be starting but why

        try sim first, 10^5 sounds interesting...

        i somehow actually remembered the intuition im a fugging genius

        61 ms runtime beats 7% tho so ill fix it now
        """

        n = len(gas)
        net = [ gas[i] - cost[i] for i in range(n) ] * 2

        """
        i move n-1 times bc i start on net[i] already
        """
        i = 0

        while i < n:
            if net[i] < 0:
                i += 1
                continue

            tot = net[i]
            j = 1

            while j < n:
                tot += net[i+j]
                if tot < 0:
                    i += j
                    break
                j += 1

            if j == n:
                return i
                
            i += 1
        
        return -1

        
            


            



