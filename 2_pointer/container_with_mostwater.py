def container_with_mostwater(height):
    l, r = 0 , len(height)-1
    best = 0
    while l< r:
        area = min(height[l],height[r])*(r-l)
        #print(height[l],height[r],(r,l))
        best = max(best,area)
        if height[l] < height[r]:
            l +=1
        else:
            r -= 1
    return best

h = [1,8,6,2,5,4,8,3,7]
print(container_with_mostwater(h))