def generate_paranthesis(n):
    ans , sol = [],[]
    def backtarck(open,close):
        if len(sol) == 2 *n:
            ans.append("".join(sol))
            return
        
        if open < n:
            sol.append("(")
            backtarck(open+1,close)
            sol.pop()

        if open > close:
            sol.append(")")
            backtarck(open,close+1)
            sol.pop()

    backtarck(0,0)
    return ans