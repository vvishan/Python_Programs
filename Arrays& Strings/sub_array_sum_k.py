def subarray_sum_k(s,k):
    count ={0:1}
    prefix = 0
    ans = 0

    for i in s:
        prefix += i
        ans += count.get(prefix-k,0)
        count[prefix] = count.get(prefix,0)+ 1
    return ans


nums = [1, 1, 1]
k = 2

print(subarray_sum_k(nums,k))