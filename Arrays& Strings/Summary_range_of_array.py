def Summary_Range(num):
    ans =[]
    i=0
    while i < len(num):
        start = num[i]
        while i < len(num)-1 and num[i]+1 == num[i+1]:
            i += 1
        if start != num[i]:
            ans. append(str(start)+"->"+str(num[i]))
        else:
            ans.append(str(num[i]))
        i += 1
    return  ans

arr = [2,3,4,5,6,8]
print(Summary_Range(arr))