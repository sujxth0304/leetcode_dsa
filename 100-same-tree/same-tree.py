# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def balanced(p, q):
            if not p and not q:
                return True

            if (q and not p) or (p and not q):
                return False
            
            if p.val != q.val:
                return False

            return balanced(p.left, q.left) and balanced(p.right, q.right)
        
        return balanced(p, q)
            
