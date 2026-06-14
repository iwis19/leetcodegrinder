# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], l: int, r: int) -> Optional[ListNode]:

        """
        LFG

        always remember on node reversal, RIGHT SIDE ORDER IS: prev, curr, curr.next, and JUST REMEMBER THAT curr.next = prev to fill the rest of the blanks

        0 ms runtime beats 100%
        """
        
        if l == r:
            return head

        start = left = right = head
        prev_left, next_right = None, None

        for i in range(1, l):
            prev_left = left
            left = left.next

        # move left once more to start and have a prev
        prev = left
        left = left.next

        for i in range(1, r):
            right = right.next
            next_right = right.next

        if prev_left:
            prev_left.next = right
        prev.next = next_right

        """
        e.g. [1,2,3,4,5] l = 2, r = 4

        5
        ^
        2 -> 3 -> 4
                  ^ 
                  1

  -------------------------------------------

        e.g. [3,5]   l = 1, r = 2
        prev_left = None, next_right = None

        None
        ^
        3 -> 5
             ^
            None
        """
        
        for _ in range(r - l):

            left.next, prev, left = prev, left, left.next
        
        """
        [1,2,3]

        l,r = 1,2 -> 2,1,3
        l,r = 1,3 -> 3,2,1
        l,r = 2,3 -> 1,3,2

        left moves when 1. l,r spans entire list, 2. l touches start
        """

        if l == 1:
            return right
        return start
