## Longest sub string without repeating the character
s = "abcabcbb"

def longest_substring(st):
    n = len(st)
    seen = set()
    l = max_len = 0
    for r in range(n):
        while st[r] in seen:
            seen.remove(st[l])
            l +=1
        seen.add(st[r])
        max_len = max(max_len, r - l +1)
    return max_len

print(longest_substring(s))

### group anagrams

words = ["bat", "tab", "cat", "act"]
from collections import defaultdict
group = defaultdict(list)
for w in words:
    group["".join(sorted(w))].append(w)
print(list(group.values()))


## Valid paranthesis

def valid_paranthesis(s):
    stack =[]
    mapping = {')':'(', ']':'[', '}':'{'}

    for i in s:
        if i in mapping.values():
            stack.append(i)
        elif i in mapping:
            if not stack and stack.pop() != mapping[i]:
                return False
    return not stack

## String_Compression ( run length encoding )
## s = aaabbc // o/p a3b2c1

s = "aaabbcc"
res =""
count = 1
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        res += s[i-1] + str(count)
        count = 1
res += s[-1] + str(count)
print(res)
