# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        """
        even though i needed editorial and gpts help, i learned more about backtracking + other things

        backtracking:
            ALMOST ALWAYS 100% RECURSION.
            the main idea of backtracking is that i:
                - try this out
                - explore consequences
                - undo the choice  -> HENCE I NEED TO USE pop. i did not know this even though i knew i had to somehow go back.
                - move onto other choice
            prev is never going to be empty and unpoppable because i append right before pop

        python reference and value types:
            mutable objs are references: e.g. sets, dicts, arrays
            immutable objs are values: int, bool, even tho they seem they are changed, its just a new value placed on it

        0 ms runtime beats 100%
        """

        res = []

        if not root:
            return res
        
        def dfs(root: Optional[TreeNode], target: int, prev: list):

            if not root:
                return

            r = target - root.val
            prev.append(root.val)

            if r == 0 and not root.left and not root.right:
                res.append(prev[:])
            else:
                dfs(root.left, r, prev)
                dfs(root.right, r, prev)

            prev.pop()

        dfs(root, targetSum, [])

        return res
