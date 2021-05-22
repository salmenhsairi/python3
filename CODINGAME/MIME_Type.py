import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mim ={}
files = []
for i in range(n):

    ext, mt = input().split()
    mim[ext.lower()] = mt
for i in range(q):
    fname = input()  
    files.append(fname)

def get_ext(f):
    ch=f
    ch2 = ""
    for c in f:
        ch2 += ch[-1]
        ch = ch[:-1]
    pos = len(f)-1-ch2.find('.')
    return f[pos+1:]

for f in files:
    if get_ext(f).lower() in mim.keys():
         print(mim[get_ext(f).lower()])
    else:
        print('UNKNOWN')

# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
#print("UNKNOWN")
