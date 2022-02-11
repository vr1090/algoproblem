# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False
        
        def sumAll(root, sumTotal):
            isLeaf = root is not None and root.left is None and root.right is None
            if isLeaf and (sumTotal+ root.val) == targetSum :
                return True
            elif root is None:
                return False
            
            return sumAll(root.left, sumTotal+root.val) or sumAll(root.right, sumTotal+root.val)
        
        return sumAll(root, 0)
        