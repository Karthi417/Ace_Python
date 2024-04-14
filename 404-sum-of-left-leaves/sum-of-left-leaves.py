# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverse(node,is_left):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                if is_left:
                    return node.val
                return 0
            return traverse(node.left,True) + traverse(node.right,False)
        return traverse(root,False)    
        