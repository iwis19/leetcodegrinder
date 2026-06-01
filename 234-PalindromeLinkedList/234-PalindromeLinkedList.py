# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        """
        okay

        kind of trash though. forgot that reverse() returned None and just reversed the actual list in place. reversed() is the right one to call. however, splicing [::-1] works on lists as well. soo
        """

        
        curr = head
        vals = []

        while curr:

            vals.append(curr.val)
            curr = curr.next

        return vals == vals[::-1]
        
