# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        def bal(node):
            
            if node == None:
                return 0 
            right = bal(node.right)
            left = bal(node.left)

            if abs(right -left) > 1:
                self.ans = False
            return 1 + max(right , left)
        bal(root)
        return self.ans