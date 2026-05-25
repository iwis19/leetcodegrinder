# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        """
        awesome sauce

        0 ms runtime beats 100%
        """

        # write a bfs first

        res = []

        q = deque()
        q.append(root)
        lvl = 0

        if not root:
            return res

        while q:

            vals = []

            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            lvl += 1

            if lvl % 2 == 0:
                vals = vals[::-1]

            res.append(vals)

        return res
