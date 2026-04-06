# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast & slow pointers
        f, s = head, head
        # loop though so long as slow and fast have next (not  =null)
        while f and f.next:
            f = f.next.next
            s = s.next
            # if fast hits slow then cycle
            if f == s:
                return True                
        
        return False
        
 