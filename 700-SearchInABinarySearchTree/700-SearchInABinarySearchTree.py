# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        """
        w recursion practice on top of bst practice

        0 ms runtime beats 100%
        """
        
        if not root:
            return None

        if val > root.val:  # go right
            return self.searchBST(root.right, val)

        elif val < root.val: # go left
            return self.searchBST(root.left, val)

        else:
            return root
