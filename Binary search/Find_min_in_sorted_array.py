def findmin(nums):
    n = len(nums)
    l = 0
    r = n-1

    while l < r:
        m = (l+ r)// 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m

    return nums[l]

nums = [4,5,6,7,0,1,2]
nums1 = [1, 2, 3, 4, 5]
print(findmin(nums))

def find_max(nums):
    n = len(nums)
    l = 0 
    r = n- 1

    while l <= r:
        mid = (l+ r)// 2
        if mid < n - 1 and nums[mid] > nums[mid + 1]:
            return nums[mid]
        if mid > 0 and nums[mid-1] > nums[mid]:
            return nums[mid-1]
        
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid -1

    return nums[r]

print(find_max(nums1))

