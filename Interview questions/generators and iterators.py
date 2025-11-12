## ITERATOR
# iterate over a sequence (one element at a time) 
# — but it doesn’t store all elements in memory at once.

nums = [2,3,4,5]
it = iter(nums)

# print(next(it))
# print(next(it))
# print(next(it))

## GENERATORS
# it is a special kind of iterator , it will create automatically when you use the 
# funtion with a Yield keyword

num1 =[3,4,5]
def generator(num):
    for i in range(len(num)):
        yield num[i]

gen = generator(num1)

print(next(gen))
print(next(gen))
