# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
        just wanted to try this pretty quick solution out 

        93 ms runtime beats 50%
        """
        
        n = 0
        dummy = ListNode(0, head)
        ptr = head

        while ptr:
            n += 1
            ptr = ptr.next

        prev, curr = dummy, head

        for i in range(n//2):
            prev, curr = prev.next, curr.next

        prev.next = curr.next

        return dummy.next



        

        
