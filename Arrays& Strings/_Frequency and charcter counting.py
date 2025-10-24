# charcter frequenct
s = "bannana"

from collections import Counter
print(Counter(s))

#--------------------------------------------------------------
# First Non Repeating character
count = Counter(s)
for ch in s:
    if count == 1:
        print(ch)
        break

#-------------------------------------------------------------
# Anagaram Check
s1,s2 = "listen", "silent"
print(sorted(s1)==sorted(s2))

#-------------------------------------------------------------
# Find all duplicates in a string

s = "programming"
print([ch for ch in set(s) if s.count(ch)> 1])