# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        best=chr(ord("z")+1)
        orda=ord("a")
        def traverse(node,current):
            if not node:
                return
            current.append(node.val)
            if node.left is None and node.right is None:
                nonlocal best
                best=min(best,"".join(reversed(list(chr(x + orda) for x in current))))
                current.pop()
                return
            traverse(node.left,current)
            traverse(node.right,current)
            current.pop()
        traverse(root,[])
        return best