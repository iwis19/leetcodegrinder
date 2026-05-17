# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        """
        learning binary trees :)

        inorder loses structure because it stores the parent node between left and right, so it loses its uniqueness, while preorder stores it before, so from top to bottom, it has its own uniqueness.
        
        0 ms runtime beats 100%
        """

        p_arr = []
        q_arr = []

        def preorder(root, arr):
            if not root:
                arr.append(None)
                return
            arr.append(root.val)
            preorder(root.left, arr)
            preorder(root.right, arr)

        preorder(p,p_arr)
        preorder(q,q_arr)
        return p_arr == q_arr
