import sys
import math

n = int(input())
CONTAINERS = []
for i in range(n):
    line = input()
    CONTAINERS.append(line)

stacks=[]
class Stack:
    def __init__(self):
        self.stack = []
    def get_stack(self):
        return self.stack
    def add_element(self,c):
        self.stack.append(c)
    def get_last(self):
        return self.stack[-1]
    def can_add(self,c):
        return (ord(c) <= ord(self.get_last()))

def choose_best(current,available):
    best = 0
    for i,c in enumerate(available):
        if(i != 0):
            if abs(ord(c) - ord(current)) < abs(ord(available[best]) - ord(current)):
                best = i
    return best

def load_in_a_stack(current):
    global stacks
    if stacks == []:
        new_stack = Stack()
        new_stack.add_element(current)
        stacks.append(new_stack)
    else:
        available_stacks = []
        for stack in stacks:
            if stack.can_add(current):
                available_stacks.append(stack)
        #choose the best stack to load on 
        if available_stacks == []:
            new_stack = Stack()
            new_stack.add_element(current)
            stacks.append(new_stack)
        else:
            headers = [stack.get_last() for stack in available_stacks]
            best_index = choose_best(current,headers)
            stack_to_be_pushed = available_stacks[best_index]
            stack_to_be_pushed.add_element(current)
    return  
 
def get_length(container):
    global stacks
    for c in container:
        load_in_a_stack(c)  
    print(len(stacks))

for container in CONTAINERS:
    get_length(container)
    stacks = []

