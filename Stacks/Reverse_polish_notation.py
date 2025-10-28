from math import ceil, floor
def reverse_polish(tokens):
    stack =[]

    for t in tokens:
        if t in '+-*/':
            b , a = stack.pop(),stack.pop()
            if t == "+":
                stack.append(a+b)
            elif t == "-":
                stack.append(a-b)
            elif t == "*":
                stack.append(a*b)
            else:
                divison = a /b
                if divison < 0:
                    stack.append(ceil(divison))
                else:
                    stack.append(floor(divison))
        else:
            stack.append(int(t))
    return stack[0]