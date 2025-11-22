class Tree:
    def __init__(self,val = 0,left=None,right =None):
        self.val = val
        self.left = left
        self.right = right
        
def lowest_common_ancestor(head:Tree,p,q):
    curr = head

    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr
