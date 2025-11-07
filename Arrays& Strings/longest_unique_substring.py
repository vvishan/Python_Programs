#Sliding Window (variable): Longest Substring Without Repeating Characters

def longest_substring(s):
    seen ={}
    l = 0
    best =0
    for r,ch in enumerate(s):
        if ch in seen and seen[ch] >= l:
            l = seen[ch] +1
            #print(l, seen[ch])  
        seen[ch] = r
        #print(r)
        best = max(best, r-l+1)
    return best

a ="abcabcbb"
print(longest_substring(a))
