class Node:
    def __init__(self,val=0,next:'Node'=None,random:'Node' =None):
        self.val = val
        self.next = next
        self.random = random


    def copy_list_random(self,head:Node):
        curr = head
        old_to_new ={}

        while curr:
            node = Node(x=curr.val)
            old_to_new[curr] = node
            curr = curr.next

        curr = head
        while curr:
            new_node = old_to_new[curr]
            new_node.next = old_to_new[curr.next] if curr.next else None
            new_node.random = old_to_new[curr.random] if curr.random else None
            curr = curr.next

        return old_to_new[head]
