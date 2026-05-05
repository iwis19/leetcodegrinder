# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        """
        need to get better at considering edge cases when it comes to linkedlists, other than that had idea correct.

        3 ms runtime beats 15% O(n*k) time complexity
        """

        # edge case [] or [1]
        if not head or not head.next: return head

        start = curr = head

        l = 0
        track = head
        while track:
            l += 1
            track = track.next
        
        t = k%l

        # rotate k%n times to save time
        for _ in range(t):

            start = curr = head

            # move to 2nd last node
            while curr.next.next:
                curr = curr.next

            # last node
            last = curr.next

            curr.next = None
            last.next = start
            head = last

        return head
        

        
