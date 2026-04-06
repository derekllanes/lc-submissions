# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        r = s.next
        prev = s.next = None

        while r:
            nxt = r.next
            r.next = prev
            prev = r
            r = nxt

        r = prev
        l = head
        while r:
            nxtR, nxtL = r.next, l.next
            l.next = r
            r.next = nxtL
            l = nxtL
            r = nxtR

