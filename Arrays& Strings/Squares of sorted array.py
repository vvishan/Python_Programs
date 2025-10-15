d = [-4,-1,0,3,10]

def sorted_array(arr):
    n = len(arr)
    result = [0] * n
    pos = n-1
    left , right = 0, n-1
    while left <= right:
        if abs(arr[left]) > abs(arr[right]):
            result[pos] = arr[left] **2
            left += 1
        else:
            result[pos] = arr[right]** 2
            right -=1
        pos -= 1
    return result

print(sorted_array(d))