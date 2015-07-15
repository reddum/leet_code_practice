# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):

    	if p.val > q.val:
    		t = p
    		p = q
    		q = t
    		
    	return self._lowestCommonAncestor(root, p, q)

    def _lowestCommonAncestor(self, root, p, q):

    	if root.val > q.val:
    		return self.lowestCommonAncestor(root.left, p, q)

    	elif root.val < p.val:
    		return self.lowestCommonAncestor(root.right, p, q)

    	else:
    		return root.val


if __name__ == "__main__":

	pass