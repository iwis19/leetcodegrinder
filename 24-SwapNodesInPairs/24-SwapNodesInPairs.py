# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        damn took me 30 mins but i solved it :)

        i tend to become impatient when i come across a bug and not as happy as before when i solve a medium. i feel like
        im starting to drift away from why i originally started leetcode. i will come back when i am more calm since i do 
        have lots of stuff on the next dday.

        also had some silly ideas / code but i realize it nowa

        0 ms runtime beats 100%
        """
        
        curr = start = head

        # also have to keep track of prev

        prev = None
        set_start = False

        while curr and curr.next:

            first, second = curr, curr.next

            first.next = second.next
            second.next = first
            if prev:
                prev.next = second

            if not set_start:
                start = second
                set_start = True

            prev = first
            curr = first.next
        
        return start
