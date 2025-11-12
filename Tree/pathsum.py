class TreeNode:
    def __init__(self,val=0,left = None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def has_pathsum(root,target):
        
        def pathsum(root,cursum):
            if not root:
                return 0
            cursum += root.val

            if not root.left or not root.right:
                return cursum == target
            return pathsum(root.left,cursum) or pathsum(root.left,cursum)
        return pathsum(root,0)