
from collections import deque
class TreeNode:
    def __init__(self,val=0,left = None,right=None):
        self.val = val
        self.left = left
        self.right = right

d ={}
word = "abcd"
for c in word:
    if c not in d:
        d[c]= {}
    d = d[c]
d['.'] ='.'
    
print(d)