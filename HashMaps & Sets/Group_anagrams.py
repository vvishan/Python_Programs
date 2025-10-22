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