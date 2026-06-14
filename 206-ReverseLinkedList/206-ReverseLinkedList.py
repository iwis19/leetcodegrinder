# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        good practice from the daily on 06/14 from earlier

        0 ms runtime beats 100% will be back
        """
        
        curr = head
        prev = None

        while curr:

            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
