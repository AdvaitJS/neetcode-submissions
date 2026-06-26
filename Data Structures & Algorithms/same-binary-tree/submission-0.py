# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def check(nodeA , nodeB):
            if nodeA is None and nodeB is None:
                return True
            if nodeA is None or nodeB is None:
                return False
            
            elif nodeA.val != nodeB.val:
                return False
            

            right_check = check(nodeA.right , nodeB.right)
            left_check = check(nodeA.left , nodeB.left)

            return left_check and right_check
        return check(p , q)