import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

speed = int(input())
light_count = int(input())
feux = []
for i in range(light_count):
    feux.append([int(j) for j in input().split()])

def check_light(feu,vitesse):
    temp_pour_arriver = (3.6 * feu[0]) / vitesse
    intervalles_verts = [[2*feu[1]*k,feu[1]*(2*k+1)] for k in range(1000)]
    for IT in intervalles_verts:
        if temp_pour_arriver >= IT[0] and temp_pour_arriver < IT[1]:
            return 1
    return 0

def check_all(vitesse):
    global feux
    for feu in feux:
         if not check_light(feu,vitesse):
                return 0
    return 1

V = speed
while V != 0:
    if check_all(V):
        print(V)
        break
    V-=1
