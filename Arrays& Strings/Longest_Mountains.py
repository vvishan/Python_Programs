def longestMountain(arr):
    n = len(arr)
    if n < 3:
        return 0

    up = 0
    down = 0
    best = 0

    for i in range(1, n):
        if arr[i] > arr[i-1]:
            # starting a new increasing run if we were descending before
            if down > 0:
                up = 0
                down = 0
            up += 1
        elif arr[i] < arr[i-1]:
            if up > 0:
                down += 1
                # valid mountain if we've had at least one up and one down
                if down > 0:
                    best = max(best, up + down + 1)
        else:  # arr[i] == arr[i-1]
            up = 0
            down = 0

    return best
arr = [2,1,4,7,3,2,5]
print(longestMountain(arr))