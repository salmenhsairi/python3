import sys
import math


n = int(input())
D = {}
for i in range(n):
    inputs = input().split()
    D[inputs[0]] = int(inputs[1])
circuit = input()
N = {}
def clean():
    global circuit
    for k in D.keys():
        if len(k) > 1:
            N[k[0]] = D[k]
            circuit = circuit.replace(k,k[0])
        else:
            N[k] = D[k]
    return

def filter_args(args):
    s = [a for a in args if a in N.keys()]
    c = [a for a in args if not a in N.keys()]
    return (s,c)

def Series(args):
    return round(sum(args),1)
def Parallel(args):
    return round(1/(sum([1/a for a in args])),1)

def solve(C):
    args = get_args(C)
    if C[0] == '[':
        if filter_args(args)[1] == [] and filter_args(args)[0] != []:
            return Parallel([N[a] for a in args])
        elif filter_args(args)[0] == [] and filter_args(args)[1] != []:
            return Parallel([solve(a) for a in filter_args(args)[1]])
        elif filter_args(args)[0] != [] and filter_args(args)[1] != []:
            return Parallel([solve(a) for a in filter_args(args)[1]] + [N[a] for a in filter_args(args)[0]])
    elif C[0] == '(':
        if filter_args(args)[1] == [] and filter_args(args)[0] != []:
            return Series([N[a] for a in args])
        elif filter_args(args)[0] == [] and filter_args(args)[1] != []:
            return Series([solve(a) for a in filter_args(args)[1]])
        elif filter_args(args)[0] != [] and filter_args(args)[1] != []:
            return Series([solve(a) for a in filter_args(args)[1]] + [N[a] for a in filter_args(args)[0]])
    
def get_args(C):
    C = C.replace(' ','')
    args = []
    i = 1
    while True:
        if C[i] in ['(','[']:
            k,l=0,0
            j=i
            while True:
                if C[j] =='(':
                    k+=1
                elif C[j] == ')' and k > 0:
                    k-=1
                if C[j] == '[':
                    l+=1
                elif C[j] == ']' and l > 0:
                    l-=1
                if C[i] == '(':
                    if C[j] == ')' and k==0 and l==0:
                        break
                elif C[i] == '[':
                    if C[j] == ']' and k==0 and l==0:
                        break
                j+=1
            args.append(C[i:j+1])
            i = j
        else:
            args.append(C[i])
        i += 1
        if i == len(C)-1:
            break
    return(args)

clean()
print(float(solve(circuit)))
# print(circuit + '\n' + str(D))

# f = frozenset()
# f |= {1,2}
# f &= {1,2,3}
# print(f)

