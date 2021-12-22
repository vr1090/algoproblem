class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Parameters:
#  root: Tree
#  num1: int
#  num2: int
# return type: Tree

def lowestCommonAncestor(root, num1, num2):
    # your code here
    if root is None:
        return None
    if root.data == num1 or root.data == num2:
        return root

    leftLca = lowestCommonAncestor(root.left, num1, num2)
    rightLca = lowestCommonAncestor(root.right, num1, num2)


    if leftLca is not None and rightLca is not None:
        return root

    if leftLca is not None:
        return leftLca
    else:
        return rightLca
