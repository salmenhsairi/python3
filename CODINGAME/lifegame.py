import sys
import math

h, w, n = [int(i) for i in input().split()]
alive = input()
dead = input()
grid = []
for i in range(h):
    grid.append(list(input()))

#grid example :
[['.','O','O','.'],['O','.','.','O'],['.','O','O','.']]
#add a padding to the grid
grid.append(['.' for k in range(h+1)])
grid.insert(0,['.' for k in range(h+1)])
for i in range(1,h):
    grid[i].append('.')
    grid[i].insert(0,'.')

def get_neighbors_list(x_idx,y_idx):
    neigh =[grid[x_idx+1,y_idx],grid[x_idx-1,y_idx],
            grid[x_idx-1:x_idx+1,y_idx+1],
            grid[x_idx-1:x_idx+1,y_idx-1]]
    return neigh
#input (x,y) -> (5,3)
# def get_neighbors_states(x_idx,y_idx):
#     alive = 0
#     for neigbor 
#     return (alive,8-alive)

#Simulation LOOP (n iterations)
#for each cell loop -> die or survive (h*w iterations)
#for each of the neihbors

print("grid")

import sys
import math

sheet = []
width, height = [int(i) for i in input().split()]
for i in range(height):
    line = input()
    sheet.append(line)

def add_zeros_padding(tab):
    buffer = ['0'+tab[k]+'0' for k in range(height)]
    buffer.insert(0,'0'*(width+2))
    buffer.append('0'*(width+2))
    return buffer

buffer = add_zeros_padding(sheet)
def get_neighbors(i,j):
    neighbors = []
    global buffer
    i,j = i+1,j+1
    neighbors.append(buffer[i-1][j-1:j+2])
    neighbors.append(buffer[i][j-1])
    neighbors.append(buffer[i][j+1])
    neighbors.append(buffer[i+1][j-1:j+2])
    return ''.join(neighbor for neighbor in neighbors)


def get_next_state(state,neighbors):
    if state == '0':
        if neighbors.count('1') == 3:
            return '1'
        return '0'
    else:
        if neighbors.count('1') in (2,3):
            return '1'
        return '0'

for i in range(len(sheet)):
    out = ''.join([get_next_state(sheet[i][j],get_neighbors(i,j)) for j in range(width)])
    print(out)










