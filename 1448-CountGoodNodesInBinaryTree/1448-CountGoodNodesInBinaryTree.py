# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0

        """
        must be monotonically increasing

        we also cannot go back to look at parent node, so we must check node.val <= node.left.val

        oops read the question as wrong as possible but got the ans very quickly after

        130 ms runtime beats 53% -> biggest optimization i made was swap maxi value in the comparison op instead of max()
        """

        def dfs(node, maxi):
            nonlocal res

            if not node:
                return

            if node.val >= maxi:
                res += 1
                maxi = node.val

            dfs(node.left, maxi)
            dfs(node.right, maxi)

        dfs(root, root.val)
        return res1
