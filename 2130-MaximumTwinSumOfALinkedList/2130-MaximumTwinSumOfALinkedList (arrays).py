# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        """
        pretty quick solution O(N) but not very fast

        82 ms runtime beats 20% 63 mb memory beats 9%
        """
        
        curr = head
        vals = [] 

        while curr:
            vals.append(curr.val)
            curr = curr.next

        print(vals)
        n = len(vals)
        res = -1

        for i in range(n//2):
            twin = vals[i] + vals[n-1-i]
            if twin > res:
                res = twin

        return res
        
