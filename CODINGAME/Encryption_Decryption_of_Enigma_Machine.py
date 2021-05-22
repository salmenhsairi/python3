import sys
import math
import string

operation = input()
pseudo_random_number = int(input())
rotors = []
for i in range(3):
    rotor = input()
    rotors.append(rotor)
message = input()
letters = string.ascii_uppercase

def chr_(o):
    global letters
    return letters[o%26]  

def ord_(c):
    global letters
    return letters.find(c)

def enigma_encode(message):
    shift = ""
    for k,c in enumerate(message):
        shift += chr_( ord_(c) + pseudo_random_number + k )
    first_rotor = ""
    for c in shift:
        alphabet_order = ord_(c)
        first_rotor+= rotors[0][alphabet_order]
    second_rotor = ""
    for c in first_rotor:
        alphabet_order = ord_(c)
        second_rotor+= rotors[1][alphabet_order]
    encoded_message = ""
    for c in second_rotor:
        alphabet_order = ord_(c)
        encoded_message+= rotors[2][alphabet_order]
    return encoded_message

def enigma_decode(message):
    second_rotor = ""
    for c in message:
        pos = rotors[2].find(c)
        second_rotor+=chr_(pos)
    first_rotor = ""
    for c in second_rotor:
        pos = rotors[1].find(c)
        first_rotor+=chr_(pos)
    shift = ""
    for c in first_rotor:
        pos = rotors[0].find(c)
        shift += chr_(pos)
    decoded_message = ""
    for i,c in enumerate(shift):
        decoded_message += chr_(ord_(c) - pseudo_random_number - i )
    return decoded_message

if (operation.upper() == 'ENCODE'):
    print (enigma_encode(message))
elif (operation.upper() == 'DECODE'):
    print (enigma_decode(message))
else :
    print(f"INVALID OPERATION : {operation}")



