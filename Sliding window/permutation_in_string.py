def permutation_string(s1,s2):
    n1 = len(s1)
    n2 = len(s2)
    s1_count =[0]*26
    s2_count =[0]*26

    if n1 > n2:
        return False
    
    for i in range(n1):
        s1_count[(ord(s1[i])- ord('a'))] += 1
        s2_count[(ord(s2[i])-ord('a'))] += 1

    if s1_count == s2_count:
        return True
    for i in range(n1,n2):
        s2_count[(ord(s2[i]-ord('a')))] += 1
        s2_count[(ord(s2[i-n1]-ord('a')))] -= 1
        if s1_count == s2_count:
            return True
    return False
