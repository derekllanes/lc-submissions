# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # check current node
        # if curr == to p or q then return
        # if curr is larger than p and q
        #   move down left subtree
        # if less than both
        #   move down right subtree
        # if curr is larger than one and smaller than the other
        #   reutrn node
        if root.val == p.val or root.val == q.val:
            print("returning")
            return root

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val < q.val or root.val < p.val and root.val > q.val:
            return root
