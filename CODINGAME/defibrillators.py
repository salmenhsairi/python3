import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = float(input().replace(',','.'))
lat = float(input().replace(',','.'))
n = int(input())

defis = []
for i in range(n):
    defib = input()
    name = defib.split(';')[1]
    latitude = defib.split(';')[-1]
    longitude = defib.split(';')[-2]
    defis.append({
          'name' : name,
          'latitude' : float(latitude.replace(',','.')),
          'longitude' : float(longitude.replace(',','.'))
    })

def distance(latitude,longitude):
    global lat
    global lon
    x = (lon - longitude)*math.cos((lat + latitude)/2)
    y = (lat - latitude)
    d = math.sqrt(x**2 + y**2)*6371
    return d
min = 0
for i,d in enumerate(defis):
    d1 = distance(defis[i]['latitude'],defis[i]['longitude'])
    if d1 < distance(defis[min]['latitude'],defis[min]['longitude']):
        min = i
      
answer = defis[min]['name']
print(answer)
