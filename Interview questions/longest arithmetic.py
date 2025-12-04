def longest_arthimetic(arr):
    n = len(arr)
    if n <= 2:
        return n
    
    res = 1
    dp = [{} for _ in range(n)]

    for i in range(n):
        for j in range(i):
            diff = arr[i]- arr[j]
            dp[i][diff] = dp[j].get(diff,1)+1
            print(dp[i][diff])
            res = max(res,dp[i][diff])
            #print(res)
    return res


x = [3,6,9,12]
print(longest_arthimetic(x))
