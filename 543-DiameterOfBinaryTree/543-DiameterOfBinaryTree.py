# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        """
        its like longest NODE.left + longest NODE.right?

        and i do this recursively from the bottom nodes

        had a good general idea, kinda needed a bit of help on combining the two functions but got there

        exact same code as 0 ms idk why its 6 ms runtime beats 28%
        """
        res = -1

        def max_depth(node):
            nonlocal res

            if not node:
                return 0

            # this gets the max # of edges for node to bottom on the left side.
            longest_left = max_depth(node.left)
            longest_right = max_depth(node.right)  # for right side

            # added up becomes the diameter at this specific node
            res = max(res, longest_left + longest_right)

            return 1 + max(longest_left, longest_right)

        max_depth(root)

        return res
