# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode | None) -> int:

        """
        wow this was easy as fudge 

        bfs is OUR beech

        12 ms runtime beats 67%
        """
        
        dq = Deque([root])

        while dq:
            level_sum = 0
            for i in range(len(dq)):
                node = dq.popleft()
                level_sum += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if not dq:
                return level_sum

        return 0
