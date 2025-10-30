class treenode:
    def __init__(self,val =0, left= None,right =None):
        self.val = val
        self.left = left
        self.right = right

    def maxdepth(self,root:treenode):
        if not root:
            return 0
        
        left = self.maxdepth(root.left)
        right = self.maxdepth(root,right)

        return 1 + max(left,right)
    