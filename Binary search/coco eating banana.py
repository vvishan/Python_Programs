from math import ceil
def eatingbanana(piles,h):
    def coco(k):
        hours = 0
        for p in piles:
            hours += ceil(p/k)
        return hours <= h
    
    l = 0
    r = max(piles)

    while l < r:
        k = (l+ r)// 2
        if coco(k):
            r = k
        else:
            l = k + 1
    return r