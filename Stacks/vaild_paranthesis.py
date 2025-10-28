def vaild_paranthesis(items):
    stack =[]
    mapping ={"(":")","{":"}","[":"]"}

    for i in items:
        if i in mapping.values():
            stack.append(i)
        elif i in mapping:
            if not stack and stack.pop() != mapping[i]:
                return False
    return not stack