num =[8,2,3,4,5]

#brute force method

def smallerthan_current(n):
    result =[]
    for i in range(len(n)):
        count = 0
        for j in range(len(n)):
            if i != j and n[j] < n[i]:
                count += 1
        result.append(count)
    return result

print(smallerthan_current(num))


##using sorting and dictnary

def smallerthan_current2(n):
    sorted_n=sorted(n)
    bucket ={}
    for i in range(len(sorted_n)):
        if sorted_n[i] not in bucket:
            bucket[sorted_n[i]] = i
            #print(bucket)
    result = [bucket[num] for num in n]
    return result

print(smallerthan_current2(num))
        