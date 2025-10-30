class treenode:
    def __init__(self,val =0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def Inverttree(self,root:treenode):
        if not root:
            return None
        root.left , root.right = root.right , root.left

        self.Inverttree(root.left)
        self.Inverttree(root.right)

        return root