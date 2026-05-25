# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        """
        needs some work but i remembered this dfs algo!

        0 ms runtime beats 100% O(N) optimal
        """
        
        left_arr, right_arr = [], []

        def trav(root,arr,is_left):
            if not root:
                arr.append("")
                return
            
            arr.append(root.val)

            if is_left:
                trav(root.left, arr, is_left)
                trav(root.right, arr, is_left)
            else:
                trav(root.right, arr, is_left)
                trav(root.left, arr, is_left)


        if root.left:
            trav(root.left, left_arr, True)
        if root.right:
            trav(root.right, right_arr, False)

        return left_arr == right_arr
            



