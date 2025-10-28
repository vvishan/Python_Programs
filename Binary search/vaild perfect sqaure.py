def valid_perfect_square(nums):
    n = len(nums)
    left = 0
    right = nums

    while left <= right:
        m = (left + right)//2
        m_squared = m * m

        if nums == m_squared:
            return True
        elif nums < m_squared:
            l = m + 1
        else:
            r = m - 1
    return False