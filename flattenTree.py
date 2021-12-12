class Tree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

# flatten the tree
def flattenTree(tree):
    if tree is None:
        return
    else:
        flattenTree(tree.left)
        flattenTree(tree.right)
        
        tempRight = tree.right

        #move the pointer here
        tree.right = tree.left

        tree.left = None
        temp = tree

        while temp.right is not None:
            temp = tree.right
        
        temp.right = tempRight


def printTree(tree,list):
    if tree is None:
        list.append(-1)
    else:
        list.append(tree.data)
        printTree( tree.left, list)
        printTree( tree.right, list)

def main():
    root = Tree(10, Tree(9), Tree(11))
    flattenTree(root)
    assert( root.left == None)
    list = []
    printTree(root, list)
    print(list)

if __name__ == "__main__":
    main()
