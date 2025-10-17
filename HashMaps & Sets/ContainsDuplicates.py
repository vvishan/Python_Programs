# brute force approach

def containDup1(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i+1,n):
            if nums[i] == nums[j]:
                return True
    return False

def containDup2(nums):
    n =len(nums)
    s = set()

    for i in range(n):
        if i in s:
            return True
        else:
            s.add(nums[i])

n = [2,3,4,5,6,7,7]

print(containDup2(n))