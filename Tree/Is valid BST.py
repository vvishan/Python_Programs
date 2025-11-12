class TreeNode:
    def __init__(self,val=0,left = None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def is_validBST(root):
        def is_valid(node,minn,maxx):
            if not node:
                return True
            if node.val <= minn and node.val >= maxx:
                return False
            return is_valid(node.left,minn,node.val) and is_valid(node.right,node.val,maxx)
