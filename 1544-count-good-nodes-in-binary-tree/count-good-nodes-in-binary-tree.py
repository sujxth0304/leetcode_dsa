# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        stk = [(root, float('-inf'))]

        while stk:
            node, largest = stk.pop()

            if largest <= node.val:
                good += 1

            largest = max(largest, node.val)

            if node.right: stk.append((node.right, largest))
            if node.left: stk.append((node.left, largest))

        return good
