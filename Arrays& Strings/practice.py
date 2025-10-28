nums = [6,7,2,15]
target = 9
seen = {}
for i, n in enumerate(nums):
    if target -n in seen:
        print(target,n)
        print([seen[target-n], i])
        break
    seen[n] = i
    print(seen)
# 2:0,7:1,11:2,15:3
#