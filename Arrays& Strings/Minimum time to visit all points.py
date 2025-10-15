## without importing the library
p=[[1,1],[3,4],[-1,0]]


def minimum_time(points):
    total_time =0
    for i in range(len(points)-1):
        x1,y1 = points[i]
        x2,y2 = points[i+1]
        dx = abs(x2-x1)
        dy = abs(y2-y1)
        total_time += max(dx,dy)
    return total_time

print(minimum_time(p))

# by importing the library

from typing import List

def minimum_visiting(points):
    total_time = 0
    for (x1,y1) ,(x2,y2) in zip(points,points[1:]):
        total_time += max(abs(x2-x1),abs(y2-y1))
    return total_time
print(minimum_visiting(p))

