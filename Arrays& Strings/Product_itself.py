def product_itself(num):
    l_mul = 1
    r_mul = 1
    n = len(num)
    l_arr = [0]*n #l_arr = [0,0,0,0]
    r_arr = [0]*n #r_arr = [0,0,0,0]

    for i in range(n):
        j = -i -1
        l_arr[i] = l_mul #l_arr = [1,1,1,1]
        r_arr[j] = r_mul #r_arr = [1,1,1,1]
        l_mul *= num[i] #l_arr = [1,1,2,6]
        r_mul *= num[j] #r_arr = [24,12,4,1]

    return [l*r for l,r in zip(l_arr,r_arr)]


arr = [1,2,3,4]
print(product_itself(arr))