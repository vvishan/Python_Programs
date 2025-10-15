s1="car"
s2 = "race"


def mergethesringsAlternatively(s1,s2):
    A= len(s1)
    B= len(s2)
    a=0
    b=0
    s =[]
    word = 1
    while a<A and b<B:
        if word == 1:
            s.append(s1[a])
            a += 1
            word = 2
        else:
            s.append(s2[b])
            b +=1
            word = 1
    while a< A:
        s.append(s1[a])
        a+=1
    while b<B:
        s.append(s2[b])
        b+=1
    return ''.join(s)


print(mergethesringsAlternatively(s1,s2))