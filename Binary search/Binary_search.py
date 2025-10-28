def binary_search(nums,target):
    n = len(nums)

    for i in range(n-1):
        if nums[i] == target:
            return i
    return -1
