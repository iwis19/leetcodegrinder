class Solution:
    def maxScore(self, parent: list[int], op: list[int], score: list[int]) -> int:

        """
        -1 0 0 0 1 2 3 3

        1 1 0 0 1 1 0 1
        
        5 6 1 2 3 2 3 -3
        """

        parent_n = len(parent)
        children = [ [] for _ in range(parent_n) ]

        for i in range(1, parent_n):
            children[parent[i]].append(i)

        def dfs(i):
            if not children[i]:
                return score[i]   # leaf node

            sums = [dfs(child) for child in children[i]]
            total = score[i] + sum(sums)
            minimum = min(sums)

            if not op[i]:
                return total - min(0, minimum)
            else:
                return total - minimum

        return dfs(0)
        
