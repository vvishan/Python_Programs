
def threesum(arr):
    arr.sort()
    n= len(arr)
    res =[]

    for i in range(n-2):
        # avoiding duplicates
        if i>0 and arr[i] == arr[i-1]:
            continue
        # optimization : if current >0 No triple sum equals 0 
        if arr[i] >0:
            break

        left = i +1
        right = n-1
        while left <right:
            s = arr[i] + arr[left]+arr[right]
            if s <0:
                left +=1
            elif s >0:
                right -= 1
            else:
                res.append([(arr[i],arr[left],arr[right])])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1
    return res

l =[-1,0,1,2,-1,-4]
print(threesum(l))