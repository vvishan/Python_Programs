def search_matrix(matrix,target):
    m = len(matrix)
    n = len(matrix[0])
    t = m * n
    l = 0
    r = t-1

    while l <= r:
        mid = (l + r)//2
        mid_i = mid //n
        mid_j = mid %n
        mid_num = matrix[mid_i][mid_j]

        if mid_num == target:
            return True
        elif mid_num < target:
            l = mid + 1
        else:
            r = mid - 1
    return False
