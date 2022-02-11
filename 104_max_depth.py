# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxJing = []
        
        def dfs(root, i):
            if root is None:
                maxJing.append(i)
            else:
                dfs(root.left, i+1)
                dfs(root.right, i+1)
        
        dfs(root,0)
        
        return max(maxJing)
        