def longestprefix(strings):
    min_length = float('inf')

    for s in strings:
        if len(s) < min_length:
            min_length = len(s)

    i= 0
    while i < min_length:
        for s in strings:
            if s[i] != strings[0][i]:
                return s[:i]
        i += 1
    return strings[0][:i]

st =["flow","flower","float"]

print(longestprefix(st))