# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isValueSame(left:Optional[TreeNode], right:Optional[TreeNode]) -> bool :
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            
            return left.val == right.val and isValueSame(left.right, right.left) and \
                isValueSame(left.left, right.right)
        
        return isValueSame(root.left, root.right)