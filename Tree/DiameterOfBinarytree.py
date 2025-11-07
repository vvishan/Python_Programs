class root:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def diameter(root):
        if not root:
            return 0
        Tdiameter=[0]
        def height(root):
            if not root:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)

            diameter = left_height + right_height
            Tdiameter[0] = max(Tdiameter[0],diameter)
            return 1 + max(left_height,right_height)
        height(root)
        return Tdiameter[0]