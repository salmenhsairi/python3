import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
def to_binary(msg):
    binaryMsg = ""
    for c in msg:
        binary = bin(ord(c))[2:] 
        while(len(binary) != 7):
            binary = "0" + binary
        binaryMsg+=binary
    return binaryMsg
bin_message = to_binary(message)
def result(mess):
    i,k = 1,0
    tab = [mess[0]+" 0"]
    while(i != len(mess)):
        if (mess[i-1] != mess[i]):
            tab.append(mess[i]+" 0")
            k+=1
        else:
            tab[k]+="0"       
        i+=1
        result = "".join(i+"," for i in tab)
        result = result.replace("0 ","00 ").replace("1 ","0 ").replace(',',' ')
    return result[:-1]
answer = result(bin_message) 
print(answer)
