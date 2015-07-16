# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
  # @param {TreeNode} root
  # @return {boolean}
  def isValidBST(self, root):

    return self.isValid(root, None, None)

  def isValid(self, root, low, high):

    if root is None:
      return True

    return (low is None or root.val > low) \
            and (high is None or root.val < high) \
            and self.isValid(root.left, low, root.val) \
            and self.isValid(root.right, root.val, high )

