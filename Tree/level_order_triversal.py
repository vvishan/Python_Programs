from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def level_order_triversal(root: TreeNode):
        if not root:
            return None
        
        queue = deque()
        queue.append(root)
        ans =[]

        while queue:
            node = queue.popleft()
            n = len(node)
            level =[]
            for i in range(n):
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(level)
        return ans

        
