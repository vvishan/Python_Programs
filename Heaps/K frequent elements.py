from collections import Counter
import heapq
def k_frequent_elements(nums,k):
    freq = Counter(nums)

    return [item for item,count in heapq.nlargest(k,freq.items(),key = lambda x :x[1])]

num = [1,1,1,2,2,3]
print(k_frequent_elements(num,2))
##opt2.  counter.most_common(k)