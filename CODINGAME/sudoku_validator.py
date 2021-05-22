import sys
import math


rows = []
for i in range(9):
    row = []
    for j in input().split():
        n = int(j)
        row.append(n)
    rows.append(row)

sub_grids = [rows[row][k:k+3] + rows[row+1][k:k+3] + rows[row+2][k:k+3] for row in (0,3,6) for k in (0,3,6)]
columns = [[rows[i][k] for i in range(9)] for k in range(9)]

def check(table):
    for i in range(1,10):
        for row in table:
            if row.count(i) != 1:
                return 0
    return 1

validate = 1
for table in [rows,columns,sub_grids] :
    if not check(table):
        validate = 0
        break               
result = 'true' if validate else 'false'
print(result)
