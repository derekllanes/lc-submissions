# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def matchTree(self, root, subRoot):
        if root == None and subRoot != None or root != None and subRoot == None:
            return False

        if root == None and subRoot == None:
            return True
        
        if root.val == subRoot.val:
            if root.left != None and subRoot.left == None or root.right != None and subRoot == None:
                return False
            
            # If there is more to search in tree
            left = self.matchTree(root.left, subRoot.left)
            right = self.matchTree(root.right, subRoot.right)

            if left == False or right == False:
                return False
            else:
                return True

        else:
            return False

            

    def match(self, root, subRoot, found):
        if root == None:
            return False

        if root.val == subRoot.val:
            found = self.matchTree(root, subRoot)

        if found == True:
            return True

        left = self.match(root.left, subRoot, found)
        if left:
            return True
        right = self.match(root.right, subRoot, found)
        if right:
            return True
        
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None:
            return True

        if root == None and subRoot != None:
            return False

        found = False

        isFound = self.match(root, subRoot, found)

        return isFound