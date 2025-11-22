def reverse_array(num,k):
    n = len(num)
    k = k % n
    print(k)

    def rev(l,r):
        while l < r:
            num[l],num[r] = num[r],num[l]
            l +=1
            r -= 1

    rev(0,n-1)
    rev(0,k-1)
    rev(k,n-1)
    return num

v =[1,2,3,4,5,6,7]

print(reverse_array(v,3))
