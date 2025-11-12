class TreeNode:
    def __init__(self,val=0,left = None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def subtree_of_another(root,subroot):

        def sametree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if (p and not q) and (q and not p):
                return False
            if p.val != q.val:
                return False
            return sametree(p.left,q.left) and sametree(p.right, q.right)
        
        def has_subroot(root):
            if not root:
                return False
            if sametree(root,subroot):
                return True
            return has_subroot(root.left) or has_subroot(root.right)
        return has_subroot(root)