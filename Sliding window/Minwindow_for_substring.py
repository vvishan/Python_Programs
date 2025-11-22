from collections import Counter
def minwindow(s,t):
    if not s and not t:
        return ""
    need = Counter(t)
    have ={}
    required = len(need)
    formed =0
    l = 0
    res = (float('inf'),0,0)

    for r,ch in enumerate(s):
        have[ch]=have.get(ch,0) + 1

        if ch in need and have[ch] == need[ch]:
            formed += 1

        while formed == required:
            if (r-l+1) < res[0]:
                res = (r-l+1,l,r)

            left_char = s[l]
            have[left_char] -= 1

            if left_char in need and have[left_char] < need[left_char]:
                formed -= 1

            l += 1

        if res[0] == float('inf'):
            return ""
        return [res[1]:res[2]+1]