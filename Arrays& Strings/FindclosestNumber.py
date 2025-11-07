def findclosestnum(num):
    closest = num[0]

    for n in num:
        if n < closest:
            closest = n

        if closest < 0 and abs(closest) in num:
            return abs(closest)
        else:
            return closest
        
nums =[-1,-1,0,2,3]
print(findclosestnum(nums))