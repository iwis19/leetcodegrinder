class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
        """
        case 1: cost1 + cost2 > costboth -> go all the way to min(need1, need2), then re-eval cost1/2 against cost both

        case 2: cost1 + cost2 < costboth -> just do singular anyw

        super good case consideration practice (1 pass)

        0 ms runtime beats 100%
        """

        cost1and2 = cost1+cost2

        if cost1and2 > costBoth:
            if need1 >= need2:
                return (need2 * costBoth + (need1 - need2) * min(costBoth, cost1))
            else:
                return (need1 * costBoth + (need2 - need1) * min(costBoth, cost2))

        return need1 * cost1 + need2 * cost2
            

            
