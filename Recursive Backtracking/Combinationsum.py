def combinationsum(num,target):
    ans,sol =[],[]
    n = len(num)
    def backtarck(i,cur_sum):
        if cur_sum == target:
            ans.append(sol[:])
            return
        if cur_sum > target  or i == n:
            return
        backtarck(i+1,cur_sum)
        
        sol.append(num[i])
        backtarck(i+1,cur_sum+num[i])
        sol.pop()
    backtarck(0,0)
    return ans