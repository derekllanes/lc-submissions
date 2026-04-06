# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkLength(self, root, res):
        if root == None:
            return 0, 0
        # Search left depth
        left, res1 = self.checkLength(root.left, res)
        # Search right depth
        right, res2 = self.checkLength(root.right, res)
        # assign node val of max num edges
        count = max(left, right)
        print(1 + count)
        res = max(res1, res2, left + right)
        # Send up
        return 1 + count, res
        
        

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        _, res = self.checkLength(root, res)
        return res
        