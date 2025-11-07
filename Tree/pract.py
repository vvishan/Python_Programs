from collections import deque

def palindromcheck(s,None_al_num: True):

    dq = deque()

    if None_al_num:
        for ch in s:
            if ch.isalnum():
                dq.append(ch.lower())

    else:
        for ch in s:
            dq.append(ch)


    while len(dq)>1:
        if dq.popleft != dq.pop():
            return False
    return True
