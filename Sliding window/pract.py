
def max_avg_of_subarray(nums,k):
    n = len(nums)
    avg = 0
    l =0

    for r in range(k):
        cur_sum += nums[r]
    max_avg = cur_sum/k

    for r in range(k,n):
        cur_sum += nums[r]
        cur_sum -= nums[r-k]

        avg = cur_sum/k

    max_av = max(max_avg,avg)
    return max_av

