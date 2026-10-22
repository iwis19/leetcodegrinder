# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:

        """
        4 AM PRE MID TERM POWERS

        11 ms runtime beats 46%
        """
        
        ans = -math.inf

        def dfs(node):
            nonlocal ans

            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # not max from every side added up, only 1 path can be chosen. either left, or right, or none.
            # replaced by node.val + max(0, left_sum, right_sum)
            # return_tot = node.val
            # if left_sum > 0 and right_sum > 0: return_tot += max(left_sum, right_sum)
            # elif left_sum > 0: return_tot += left_sum
            # elif right_sum > 0: return_tot += right_sum

            ans = max(ans, node.val + max(0, left_sum) + max(0, right_sum))

            return node.val + max(0, left_sum, right_sum)

        dfs(root)
        return ans
