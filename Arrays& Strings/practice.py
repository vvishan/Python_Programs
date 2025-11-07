from collections import defaultdict
from collections import Counter
from math import ceil
def smallerthancurrent(nums):
    bucket ={}
    sorted_num = sorted(nums)
    res =[]

    for i in range(len(nums)):
        if sorted_num[i] not in bucket:
            bucket[sorted_num[i]] = i
    
    for num in nums:
        res.append(bucket[num])
    return res 
num =[8,2,3,4,5]
print(smallerthancurrent(num))
        

    