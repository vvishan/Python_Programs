class Tree:
    def __init__(self,val=0,left= None,right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
def serialize(root:Tree):
    d = deque([root])
    res =[]

    while d:
        node = d.popleft()
        if node:
            res.append(str(node.val))
            d.append(node.left)
            d.append(node.right)
        else:
            res.append("null")

    return ''.join(res)

def deserialize(data):
    if data == "null":
        return None
    node = data.split(",")
    root = Tree(int(node[0]))
    q = deque([root])
    i = 1
    while q:
        nodes = q.popleft()
        if node[i] != "null":
            nodes.left = Tree(int(node[i]))
            q.append(nodes.left)
        i += 1

        if node[i] != "null":
            nodes.right = Tree(int(node[i]))
            q.append(nodes.right)
        i += 1
    return root
            