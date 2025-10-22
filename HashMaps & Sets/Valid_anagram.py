from collections import Counter

def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    
    s_dict = Counter(s)
    t_dict = Counter(t)

    return s_dict == t_dict


s= "anagram"
t= "nagrama"

print(valid_anagram(s,t))