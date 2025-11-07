def merge_intervals(intervals):
    intervals.sort(key= lambda interval : interval[0])
    merge =[]

    for interval in intervals:
        if not  merge or merge[-1][1] < interval[0]:
            merge.append(interval)
            #print(merge)
        else:
            merge[-1]= [merge[-1][0],max(merge[-1][1],interval[1])]
            
    return merge

 
        
vals =[[5, 10], [1, 3], [2, 6]]
print(merge_intervals(vals))