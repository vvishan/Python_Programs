def binary_search(nums,target):
    n = len(nums)

    for i in range(n-1):
        if nums[i] == target:
            return i
    return - 1


def search_insert_position(nums,val):
    n = len(nums)
    l = 0
    r = n-1

    while l <= r:
        mid = (l + r) //2
        if nums[mid] < val:
            l = mid + 1
        elif nums[mid] > val:
            r = mid -1
        else: 
            return mid

    if nums[mid] < val:
        return mid + 1
    else:
        return mid
    
def search_2D_matrix(matrix,target):
    m = len(matrix)
    n = len(matrix[0])
    t = m *n
    l = 0
    r = t-1

    while l <= r:
        mid = (l+ r)//2
        mid_i = mid // n
        mid_j = mid % n
        mid_num = matrix[mid_i][mid_j]
        if mid_num == target:
            return True
        elif mid_num < target:
            l = mid + 1
        else:
            r = mid -1
    return False

def vaild_squares(nums):
    l = 0
    r = nums

    while l < r:
        m = (l+ r) // 2
        m_squared = m * m
        if nums == m_squared:
            return True
        elif nums < m_squared:
            l = m + 1
        else:
            r = m - 1
    return False




    