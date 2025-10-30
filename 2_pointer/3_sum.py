## with Hashmap

def three_sum(nums):
    h ={}
    s = set()
    n = len(nums)

    for i, num in enumerate(nums):
        h[num] = i
        #print(h)

    for i in range(n):
        for j in range(i+1,n):
            desired = -nums[i] -nums[j]
            #print(desired,nums[i],nums[j])
            if desired in h and h[desired]!= i and h[desired]!= j:
                s.add(tuple(sorted([nums[i],nums[j],desired])))
    return s

input = [-1, 0, 1, 2, -1, -4]
print(three_sum(input))
