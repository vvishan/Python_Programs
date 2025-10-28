## Brute Force Approach
def reverse_string(st):
    n = len(st)
    # l = 0
    # r = n -1
    res =""

    for i in range(n-1,-1,-1):
        res += st[i]

    return res

s = "hello"
#print(reverse_string(s))
str = ["h", "e", "l", "l", "o"]
### 2 Pointer approach

def resverse_string2(st):
    n = len(st)
    l = 0
    r = n-1

    while l < r:
        st[l],st[r] = st[r],st[l]
        l += 1
        r -= 1
    return st

print(resverse_string2(str))