def two_sum(nums,target):
    n = len(nums)
    l =0
    r = n-1

    while l < r:
        tsum = nums[l] + nums[r]
        if tsum == target:
            return(l+1,r+1)
        elif tsum < target:
            l +=1
        else:
            r -= 1
            