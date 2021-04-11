# The sotrage class for creation

class _BinTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def preorderTrav( subtree ) :
        if subtree is not None :
            print( subtree.data)
            preorderTrav( subtree.left )
            preorderTrav( subtree.right)


