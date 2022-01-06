import sys
import math

n = int(input())
T = []
cache = [None for i in range(n)]
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    T.append((operation, arg_1, arg_2))

def solve(i,operation,arg_1,arg_2):
    if operation == "VALUE":
        res = eval(arg_1)
    elif operation == "ADD":
        res = eval(arg_1) + eval(arg_2)
    elif operation == "SUB":
        res = eval(arg_1) - eval(arg_2)
    elif operation == "MULT":
        res = eval(arg_1) * eval(arg_2)
    cache[i] = res
    return (res)

def eval(arg):
    if "$" in arg:
        index = int(arg.replace('$',''))
        return cache[index] if cache[index] != None else solve(index,T[index][0],T[index][1],T[index][2])
    return int(arg)

for i,(operation, arg_1, arg_2) in enumerate(T):
    s = solve(i,operation,arg_1,arg_2)
    print(s)

D = int(input('Donner la Distance Totale'))
n = int(input('Donner le nombre d intervalles'))
T = []
for i in range(n):
    x,y = input().split()
    T.append((x,y))

# import sys
# import math

# w, h = [int(i) for i in input().split()]
# L = []
# for i in range(h):
#     line = input()
#     L.append(line)
# T = L[0]
# B = L[-1]
# def start_from(idx):
#     r = 1
#     c = idx
#     while(L[r].find('|') != -1 and r < h):
#         if (c < w-1 and L[r][c+1] == '-') :
#             c+=3
#         elif (c > 0 and L[r][c-1] == '-') :
#             c-=3
#         r += 1
#     return c
# for i,k in enumerate(T):
#     if k != ' ':
#         print(f'{k}{B[start_from(i)]}')

# import sys
# import math

# n = int(input())
# D = {}
# for i in range(n):
#     inputs = input().split()
#     D[inputs[0]] = int(inputs[1])
# circuit = input()

# def Series(args):
#     return round(sum(args))
# def Parallel(args):
#     return round(1/(sum([1/a for a in args])))

# def solve(circuit):
#     pass


class Circuit:
    def __init__(self, data):
        self.children = []
        self.data = data
    
    def __str__(self) -> str:
        if self.data == 'P':
            s = '[ '+' '.join([c.__str__() for c in self.children])+' ]'
        elif self.data == 'S':
            s = '( '+' '.join([c.__str__() for c in self.children])+' )'
        return s
    
    def parse(circuit):
        if circuit.startswith('['):
            circuit = circuit[2:-2]
            args = circuit.split() 



c2 = Circuit('S')
c2.children = ['A','B']

c1 = Circuit('P')
c1.children = ['C','A']

c0 = Circuit('P')
c0.children = [c1,c2]

print(c0.__str__())





