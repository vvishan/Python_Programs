
from collections import deque
class TreeNode:
    def __init__(self,val=0,left = None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def lowestcommonancestor(root,p,q):
        lca = [0]
        def search(root):
                
                if not root:
                    return
                lca[0] = root
                if root is p or root is q:
                    return False
                elif p.val<root.val and q.val < root.val:
                    search(root.left)
                elif p.val > root.val and q.val > root.val:
                    search(root.right)
                else:
                    return
                
        search(root)
        return lca[0]

