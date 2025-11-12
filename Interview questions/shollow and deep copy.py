import copy
## shallow copy
list = [[1, 2], [3, 4]]
shallowcopy = copy.copy(list)
print(list,shallowcopy)

shallowcopy[0][0] = 20
print(list,shallowcopy)

## Deep COPY

list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)
print(list1,list2)
list2[0][0] = 70
print(list1,list2)