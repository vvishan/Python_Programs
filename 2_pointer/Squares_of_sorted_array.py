def squares_of_sorted_array(nums):
    n = len(nums)
    l = 0
    r = n-1
    result =[]

    while l < r:
        if abs(nums[l])  > abs(nums[r]):
            result.append(nums[l]**2)
            l += 1
        else:
            result.append(nums[r]**2)
            r -= 1
    result.reverse()
    return result
n= [-4, -1, 0, 3, 10]
print(squares_of_sorted_array(n))