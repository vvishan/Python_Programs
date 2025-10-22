from collections import defaultdict
def maximumballoons(s):
    counter = defaultdict(int)
    ballon = 'balloon'

    for i in s:
        if i in ballon:
            counter[i] += 1
    
    if any(c not in counter for c in ballon):
        return 0
    else:
        return min(counter['b'],counter['a'],counter['l']//2,counter['o']//2,counter['n'])
    
d= "loonbalxballpoon"
print(maximumballoons(d))

