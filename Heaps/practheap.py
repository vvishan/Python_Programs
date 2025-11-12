import heapq
num=[7,5,2,3,6,8,8,9]

def kclosestpointstoorigin(points,k):
    def distance(x,y):
        return x**2 + y**2
    heap=[]
    for x,y in points:
        d = distance(x,y)
        if len(heap)< k:
            heapq.heappush(heap,-d,x,y)
        else:
            heapq.heappushpop(heap,-d,x,y)
    return[(x,y) for d,x,y in heap]
