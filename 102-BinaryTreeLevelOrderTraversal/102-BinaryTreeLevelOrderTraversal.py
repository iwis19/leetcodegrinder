# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        """
        bfs algo learning !1! 1!1

        since its level traversal, breadth is the most reasonable and as we are in each breadth we add it in, queue is the method to go.

        0 ms runtime beats 100%
        """
        
        res = []

        if not root:
            return res

        queue = collections.deque()
        queue.append(root)

        while queue:

            level = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level)

        return res
            

            

        
