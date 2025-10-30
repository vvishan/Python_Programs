def trap_rainwater(nums):
    n = len(nums)
    l_wall = r_wall =0
    max_left = [0]*n
    max_right =[0]*n

    for i in range(n):
        j = -i -1
        max_left[i] = l_wall
        max_right[j]= r_wall
        
        l_wall = max(l_wall,nums[i])
        r_wall = max(r_wall,nums[j])
        print(max_left)

    summ =0
    for i in range(n):
        pot = min(max_left[i],max_right[i])
        print(pot,max_left[i],max_right[i])
        summ += max(0,pot - nums[i])
    return summ

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap_rainwater(heights))