def day_temperatures(temp):
    n= len(temp)
    stack =[]
    answer = [0]*n

    for i,t in enumerate(temp):
        while stack and stack[-1][0] < t:
            stack_t, stack_i = stack.pop()
            answer[stack_i] = i - stack_i

        stack.append((t,i))
    return answer    

input =[73, 74, 75, 71, 69, 72, 76, 73]
print(day_temperatures(input))