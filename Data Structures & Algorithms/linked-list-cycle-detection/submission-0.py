# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Make seen set
        seen = set()
        # Get nodes
        curr = head

        # loop through
        while curr and curr.next:
            # check next pointer
            # if next pointer in seen
            if curr.val in seen:
                return True
            # Else add node
            else:
                seen.add(curr.val)
            curr = curr.next

        return False