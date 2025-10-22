## example s="acf" and t ="abcdef" here we need to find the sequence of words present in s from t and making sure that the t > s in the len
def Issequence(s,t):
    S = len(s)
    T = len(t)
    if s == '': return True
    if S > T : return False

    j=0
    for i in range(T):
        if t[i]==s[j]:
            if j == S-1:
                return True
            j += 1
    return False

s="acf" 
t ="abcdef"
print(Issequence(s,t))