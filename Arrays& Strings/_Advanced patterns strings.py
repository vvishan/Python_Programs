## finding subsequence exits:

def is_subsequence(s,t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j +=1
        i+=1
    return j == len(s)


## find all palindromic substrings

# s = "aaa"
# count =0

# for i in range(len(s)):
#     for j in range(i,len(s)):
#         if s[i:j+1] == s[i:j+1][::-1]:
#             count += 1
# print(count)

##  Minimu Window substring 
## here in a given text we need to find the patterns
from collections import Counter,defaultdict
def min_window(s,t):
    if not s or not t:
        return ""
    need = Counter(t)
    print(need)
    window = defaultdict(int)
    required = len(need)
    print(required)
    formed = 0

    #tuple for window lwngth,left,right
    ans =(float('inf'),None,None)

    l =0
    for r,ch in enumerate(s):
        window[ch] += 1
        print(window)

        if ch in need and window[ch]==need[ch]:
            formed += 1
        while l <= r and formed == required:
            if (r-l+1) < ans[0]:
                ans = (r-l+1,l,r)
                print(ans)
                print(formed)
        # remove the left char and move the left pointer
            left_char = s[l]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                formed -= 1
                print(formed)
            l+=1
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2]+1]

s = "ADOBECODEBANC"
t = "ABC"

print(min_window(s,t))