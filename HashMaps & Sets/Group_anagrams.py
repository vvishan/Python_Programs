from collections import defaultdict
def group_anagrams(str):
    anagram_list = defaultdict(list)
  

    for s in str:
        count = [0]* 26
        for i in s:
            count[(ord(i)-ord('a'))] += 1

        key = tuple(count)
        anagram_list[key].append(s)

    return anagram_list.values() 

st =["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(st))

## alternate way

def group_anagram2(str):
    group_list={}

    for s in str:
        key = ''.join(sorted(s))
        
        if key not in group_list:
            group_list[key] =[]
    
        group_list[key].append(s)
    return group_list.values()


print(group_anagram2(st))