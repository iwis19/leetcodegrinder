# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        """
        awesome saucey cuz i did it myself this time instead of last time HHOOHOHOHHO

        lowkey not the best at recursions where i need to return values rather than backtracking where i just act on a grid

        but still made it through ill work on it more

        mainly just forgetting to return at the base cases (only remembering to return when i see a value i want / need
        
        68 ms runtime beats 23%)
        """
        
        def isSameTree(root1, root2):
            if not root1 and not root2:
                return True

            if not root1: return False
            if not root2: return False

            if root1.val != root2.val: return False

            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)

        def dfs(node):
            if not node:
                return False

            if isSameTree(node, subRoot):
                return True

            return dfs(node.left) or dfs(node.right)

        return True if dfs(root) else False
            
