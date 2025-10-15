def romtoint(s):
    d = {'I': 1,'V':5,'X':10,'L':50,'C':100,'D':150}
    total =0
    n= len(s)
    i=0
    while i < n:
        if i<n-1 and d[s[i]] < d[s[i+1]]:
            total += d[s[i+1]] - d[s[i]]
            i += 2
        else :
            total += d[s[i]]
            i += 1
    return total


s ="XVXX"
print(romtoint(s))