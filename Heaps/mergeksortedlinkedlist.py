import heapq
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

    
def linkedlistdata(lists:ListNode):

    heap =[]

    for i, node in enumerate(lists):
          if node:
            heapq.heappush(heap, (node.val,i,node))
    
    D = ListNode()
    cur = D

    while heap:
        val,i,node = heapq.heappop(heap)
        cur.next = node
        cur = node
        node = node.next
        if node:
            heapq.heappush(heap,(node.val,i,node))
    return D.next.val

lis = [[2,4,3],[1,2,3],[3,6,7]]

def buildlinkedlist(arr):
    linked = ListNode(arr[0])
    cur = linked
    for val in arr:
        cur.next = ListNode(val)
        cur = cur.next
    return linked

link = [buildlinkedlist(val) for val in lis]

print(linkedlistdata(link))