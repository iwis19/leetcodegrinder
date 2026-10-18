class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:

        """
        obviously cannot run simulation for each possible root node

        looking at example 1: [3,1][3,2][1,4][2,0]
        then we have BRRWB, so: [W,R][W,R][R,B][R,B]

        looking at example 2: [0,1][1,2][2,3]
        we have RBRB, so: [R,B][B,R][R,B]

        important clue is to get the indegree and outdegree of each node
        """

        n = len(colors)
        indegree = [0] * n
        outdegree = [0] * n

        order = {"R": 0, "B": 1, "W": 2}

        for u, v in edges:
            if colors[u] == colors[v]:
                return -1

            # this means u -> v, so indeg +1 for v, outdeg +1 for u
            if (order[colors[u]] + 1) % 3 == order[colors[v]]:
                outdegree[u] += 1
                indegree[v] += 1
            else:
                outdegree[v] += 1
                indegree[u] += 1

        ans = -1
        
        for i in range(n):
            if indegree[i] > 1 or outdegree[i] > 2:
                return -1

            if indegree[i] == 0:
                ans = i

        return ans
        
