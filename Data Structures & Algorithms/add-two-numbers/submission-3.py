# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        currOne, currTwo = l1, l2
        res = ListNode()
        head = res

        while currOne or currTwo:
            a = 0 if currOne is None else currOne.val
            b = 0 if currTwo is None else currTwo.val


            total = a + b + carry

            currRes = ListNode(total % 10)

            carry = total // 10

            if currOne:
                currOne = currOne.next
            if currTwo:
                currTwo = currTwo.next

            res.next = currRes
            res = res.next

        if carry:
            res.next = ListNode(1)
        
        return head.next


