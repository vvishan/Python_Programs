def longest_repeating(nums):
    n = len(nums)
    l = 0
    max_length = 0
    s = set()

    for r in range(n):
        if nums[r] in s:
            s.remove(nums[l])
            l += 1
        w = r- l + 1
        max_length = max(max_length,w)
        s.add(nums[r])
    return max_length