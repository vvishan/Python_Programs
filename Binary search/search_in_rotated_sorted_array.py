## Find the index of a target value in a sorted array that has been rotated an unknown number of times,
#  or return -1 if not found.

def search_index(nums, target):
    n = len(nums)
    l = 0
    r = n-1

    while l < r:
        mid = (l+ r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid

    num_i = l

    if num_i == 0:
        l , r = 0, n-1
    elif target >= nums[0] and target <= nums[num_i - 1]:
        l, r = 0 , num_i - 1
    else:
        l , r = num_i, n-1

    while l <= r:
        m = (l + r)// 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
