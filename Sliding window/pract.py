s = "AABBCA"
count =[0]*26
for i in s:
    count[(ord(i)-65)] += 1
print(count)

