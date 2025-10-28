def Is_badversion(version,bad):
    return version>=bad

def first_bad_version(nums):
    left, right = 0,len(nums)
    while left <= right:
        mid =(left + right) // 2
        if Is_badversion(mid):
            right = mid
        else:
            left = mid + 1
    return left
