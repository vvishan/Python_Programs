r =[3,4,5,6,7,8]

def twosum(num,target):
    #two pointer approach
    n = len(num)
    left = 0
    right = n-1
    s =[]

    while left < right:
        tsum = num[left]+num[right]
        if tsum == target:
            s.append([left,right])
            left+=1
            right-=1
        elif tsum < target:
            left += 1
        else:
            right -=1
    return s

print(twosum(r,7))

