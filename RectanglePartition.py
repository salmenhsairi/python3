import sys
import math

width, height, count_x, count_y = [int(i) for i in input().split()]
measures_x = []
for i in input().split():
    x = int(i)
    measures_x.append(x)
measures_y = []
for i in input().split():
    y = int(i)
    measures_y.append(y)

measures_x.insert(0,0) 
measures_x.append(width)

measures_y.insert(0,0) 
measures_y.append(height)

def final_measures(measures):
    final_measures = measures[1:]
    for i,m in enumerate(measures[1:]):
        for prev in measures[1:i+1]:
            final_measures.append(m-prev)
    return final_measures

final_x = final_measures(measures_x)
final_y = final_measures(measures_y)

n = 0
for e_y in final_y:
    n+= final_x.count(e_y) 

print(n)
