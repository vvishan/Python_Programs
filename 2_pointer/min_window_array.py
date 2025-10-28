from collections import defaultdict
def min_window_array(arr):
    n = len(arr)
    distnict_count = len(set(arr))
    #print(distnict_count)
    count = defaultdict(int)
    left = 0
    formed =0
    min_len = n+1

    for right in range(n):
        count[arr[right]] += 1
        if count[arr[right]] == 1:
            formed += 1
            

        while formed == distnict_count:
            min_len = min(min_len,right-left+1)
            
            count[arr[left]] -= 1

            if count[arr[left]] == 0:
                formed -= 1
            left += 1
    return 0 if min_len == n + 1 else min_len
    
ar = [7,3,4,1,3]
print(min_window_array(ar))


