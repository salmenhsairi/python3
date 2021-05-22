import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
ps = []
for i in range(n):
    pi = int(input())
    ps.append(pi)

ps.sort()
m = ps[1] - ps[0]
for i in range(1,len(ps)):
    diff = ps[i] - ps[i-1]
    if diff < m:
        m = diff
print(m)
