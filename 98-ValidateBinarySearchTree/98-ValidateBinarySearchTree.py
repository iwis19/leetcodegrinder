# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        """
        bfs solution first

        learned to set boundaries while appending each node into the queue, use an array and put everything in. or just generally, i can just use an array to sotre more into that i might need.

        0 ms runtime beats 100% 
        """

        q = deque()
        q.append([root, -math.inf, math.inf])

        while q:

            for _ in range(len(q)):
                node, low, high = q.popleft()
                parent_val = node.val

                if node.left:
                    if not low < node.left.val < parent_val:
                        return False
                    q.append([node.left, low, parent_val])
                
                if node.right:
                    if not parent_val < node.right.val < high:
                        return False
                    q.append([node.right, parent_val, high])

        return True
