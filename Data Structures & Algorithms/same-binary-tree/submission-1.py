# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    res = True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None and q != None or p != None and q == None or self.res == False:
            self.res = False
            return False

        
        
        if p.val != q.val or self.res == False:
            self.res = False
            return False

        check = self.isSameTree(p.left, q.left)

        check = self.isSameTree(p.right, q.right)

        return self.res

        

        

