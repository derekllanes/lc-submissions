# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkNodes(self, node, maxNode, count):
        if node == None:
            return 0

        if node.val >= maxNode:
            count += 1
            maxNode = node.val

        left = self.checkNodes(node.left, maxNode, 0)
        right = self.checkNodes(node.right, maxNode, 0)

        count += left + right
        return count


    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0

        res = 1
        maxNode = root.val

        left = self.checkNodes(root.left, maxNode, 0)
        right = self.checkNodes(root.right, maxNode, 0)

        return res + left + right

