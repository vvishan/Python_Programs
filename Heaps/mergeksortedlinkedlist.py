import heapq
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

    
def linkedlistdata(lists:ListNode):

    heap =[]

    for i, node in enumerate(lists):
          if node:
            heapq.heappush(heap,(node.val,i,node))
    return heap
def build_linkedlist(arr):
    dummy = ListNode(arr[0])
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy

lis = [[2,4,3],[1,2,3],[3,6,7]]
linkedlist = [build_linkedlist(a) for a in lis]

print(linkedlistdata(linkedlist))