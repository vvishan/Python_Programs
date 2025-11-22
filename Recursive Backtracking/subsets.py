def subset(nums):
    n = len(nums)
    res ,sol = [],[]

    def backtracking(i):
        if i == n:
            res.append(sol[:])
            return

        #dont pick
        backtracking(i+1)

        # pick
        sol.append(nums[i])
        backtracking(i+1)
        sol.pop()
    backtracking(0)
    return res
