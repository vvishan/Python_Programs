def containsnearbyDuplicates(s,k):
    num_to_i = {}
    n = len(s)

    for i in range(n):
        if s[i] in num_to_i:
            if abs(num_to_i[s[i]]-i) <= k:
                return True
    return False