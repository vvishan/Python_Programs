def combinationsum(nums,target):
    ans, sol = [],[]
    n = len(nums)

    def backtrack(i,cur_sum):
        if cur_sum == target:
            ans.append(sol[:])
            return
        if cur_sum > target and i == n:
            return
        backtrack(i+1,cur_sum)

        sol.append(nums[i])
        backtrack(i+1,cur_sum+nums[i])
        sol.pop()
    backtrack(0,0)
    return ans
