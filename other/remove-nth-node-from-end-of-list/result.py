# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head
        # move right to create the gap
        while n > 0:
            right = right.next
            n-=1

        # move both at the same time until end
        while right:
            right = right.next
            left = left.next

        # remove node(s)
        left.next = left.next.next

        return dummy.next
