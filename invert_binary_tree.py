# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        
        if root == None:
            return root
        
        left = root.left
        right = root.right
        
        if right != None:
            root.left = self.invertTree(right)
        else:
            root.left = right
        
        if left != None:
            root.right = self.invertTree(left)
        else:
            root.right = left
        
        return root
        