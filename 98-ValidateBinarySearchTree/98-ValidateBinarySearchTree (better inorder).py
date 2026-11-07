# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        """
        was gonna dfs entire tree but this was sm better thank goodness i thought of it

        0 ms runtime beats 100%
        """
        
        inorder = []

        def dfs(node):
            
            if node:
                dfs(node.left)
                inorder.append(node.val)
                dfs(node.right)

        dfs(root)

        for i in range(1, len(inorder)):
            if inorder[i] <= inorder[i-1]:
                return False

        return True
