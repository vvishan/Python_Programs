arr =[2,1,4,7,3,2,5]

def twosum(arr,target):
    arr= sorted(arr)
    n = len(arr)
    res =[[arr],]
    # two pointer appraoch

    left = 0
    right = n-1
    while left < right:
        tsum = arr[left]+ arr[right]
        if tsum == target:
            res. append([left,right])
            left +=1
            right -= 1
        elif tsum < target:
            left +=1
        else:
            right -= 1
    return res

print(twosum(arr,10)) 


