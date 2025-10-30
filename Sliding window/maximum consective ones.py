##Find the maximum number of consecutive 1s in a binary array if at most k zeros can be flipped to 1
def max_consucutive_ones(nums,k):
    n = len(nums)
    max_w =0
    max_zeros =0
    l =0

    for r in range(n):
        if nums[r]==0:
            max_zeros += 1
        if max_zeros > k:
            if nums[l] == 0:
                max_zeros -= 1

            l += 1
        w = r - l+ 1
        max_w = max(max_w,w)
    return max_w 
