'''Importing operating system module'''
import os

class Stack:
  
    def __init__(self, size):
        self.items = []
        self.size = size
        
''' This function is used to return if the stack is empty'''
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
'''This function is used to return if the stack is full'''
    def is_full(self):
        if len(self.items) == self.size:
            return True
        else:
            return False
        
'''function to push data into the stack'''
    def push(self, data):
        if not self.is_full():
            self.items.append(data)
''' function to pop elements in the stack from top'''
    def pop(self):
        if not self.is_empty():
            # Write code here
            self.items.pop()
'''to display all the elements in the stack'''
    def status(self):
        for element in self.items:
            print(element)

'''inputting size and queries for the user'''
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
