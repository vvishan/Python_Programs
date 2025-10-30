def longest_substring(st):
    n = len(st)
    max_length = 0
    l = 0
    s = set()
    
    for r in range(n):
        while st[r] in s:
            s.remove(st[l])
            l += 1
        w = r - l + 1

        max_length = max(max_length,w)
        s.add(s[r])

    return max_length