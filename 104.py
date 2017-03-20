# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def lcr(node, c):
            l = c
            r = c
            if node.left is not None:
                l = lcr(node.left, c + 1)
            if node.right is not None:
                r = lcr(node.right, c + 1)
            return max(l, c, r)
        
        if root is not None:
            return lcr(root, 1)
        return 0
        
