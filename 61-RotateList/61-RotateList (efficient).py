# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        """
        took the better approach, non brute force, creates a loop and chooses the right spot to break

        0 ms runtime beats 100% O(n)
        """

        # edge case [] or [1]
        if not head or not head.next: return head

        last = head

        l = 1
        while last.next:
            last = last.next
            l += 1

        # makes loop
        last.next = head

        # cut off tie between l-(k%l) th and l-(k%l)+1 th node
        n = l - k%l

        curr = head
        for i in range(n-1):
            curr = curr.next

        new_head = curr.next
        curr.next = None
       
        return new_head


       
