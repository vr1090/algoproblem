class Tree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
# Parameters:
#  root: Tree
#  num1: int
#  num2: int
# return type: Tree

def lowestCommonAncestor(root, num1, num2):
    listPathLeft=[]
    listPathRight = []

    if not findPath(root, listPathLeft, num1) or  not findPath(root, listPathRight, num2):
        return None
    
    minLength = min( len(listPathLeft), len(listPathRight))

    i = 0
    index = 0

    while i < minLength:
        if listPathLeft[i] == listPathRight[i]:
            index = i
            i += 1
        else:
            break

    return listPathLeft[index]        



def findPath(root, listParent, num):
    if root is None:
        return False
    
    listParent.append(root)

    if root.data == num:
        return True

    if findPath(root.left, listParent, num) or \
      findPath(root.right, listParent,num ):
      return True
    
    #did not work
    listParent.pop()
    return False