class Tree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
# Parameters:
#  root: Tree
# return type: int

def maxPathSum(root):
    return dfs(root,[float("-inf")] )


def dfs(root, globalMaxSum):
    if root is None:
        return float("-inf")
    else:
        left = dfs(root.left, globalMaxSum)
        right = dfs(root.right, globalMaxSum)
        maxTop =max(root.data, root.data + left, root.data + right)
        maxNoTop = max( maxTop, root.data + left + right)
        # update global
        globalMaxSum[0] = max( globalMaxSum[0], maxNoTop)

        return maxTop
