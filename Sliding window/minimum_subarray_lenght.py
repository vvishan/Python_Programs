#Find the length of the shortest contiguous subarray with a sum greater than or 
# equal to a given target, or return 0 if none exists.

def minimum_subarray(nums, target):
    n = len(nums)
    min_length = float('inf')
    l = 0
    summ = 0

    for r in range(n):
        summ += nums[r]
        while summ >= target:
            min_length = min(min_length,r-l+1)
            summ  -= nums[l]
            l += 1
    return min_length if min_length < float('inf') else 0
