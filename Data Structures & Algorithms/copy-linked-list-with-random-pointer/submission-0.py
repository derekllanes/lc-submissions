"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        curr = head
        nodeMap = {}

        while curr != None:
            nodeMap[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr != None:
            if curr.random == None:
                nodeMap[curr].random = None
            else:
                nodeMap[curr].random = nodeMap[curr.random]
            if curr.next == None:
                nodeMap[curr].next = None
            else:
                nodeMap[curr].next = nodeMap[curr.next]
            curr = curr.next

        return nodeMap[head]
