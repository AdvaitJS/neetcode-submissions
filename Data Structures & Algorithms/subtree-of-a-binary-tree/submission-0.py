# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSub(node , sub):
            if node is None and sub is None:
                return True
            elif node is None and sub is not None:
                return False
            elif node is not None and sub is None:
                return False
            elif node.val != sub.val:
                return False
            else:

                left_check = isSub(node.left , sub.left)
                right_check = isSub(node.right , sub.right)

                return (left_check and right_check)
        
        if root is None:
            return False
        if isSub(root , subRoot):
            return True
        return (
                self.isSubtree(root.left, subRoot)
                    or
                self.isSubtree(root.right, subRoot)
                )
            