from collections import deque
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
    
    def maaxdepth2(self,root:treenode):
        level = 0
        if not root: return 0
        q = deque([root])
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            level += 1
        return level