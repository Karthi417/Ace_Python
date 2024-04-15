# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(node,current):
            if node is None:
                return 0
            current *= 10
            current += node.val
            if node.left is None and node.right is None:
                return current
            return traverse(node.left,current) + traverse(node.right,current)
        return traverse(root,0)       