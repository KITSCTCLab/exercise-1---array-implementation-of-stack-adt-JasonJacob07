"""Importing operating system module"""
import os

class Stack:
""" Creation of a class called Stack. This class includes all the necessary stack operations. This class contains 6 necessary function for the Operation of stack.
1st. to intialize size of the stack with the Stack class(max size of the stack)
2nd. A function to  check if the stack is empty(Stack underflow).
3rd. A function to check if the stack is full(Stack overflow).
4th. A function to push(add) elements in the stack.
5th. A function to pop(remove) elements in the stack.
6th. A function to show the elements present in the stack line by line"""

"""Attributes:
    size = To ensure the max size of the stack
    items = to add  elements in the stack for stack operation """

"""Initializing items and size with the class Stack"""
    def __init__(self, size):
        self.items = []
        self.size = size

"""This function is used to return if the stack is empty"""
    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
          return False
        
"""This function is used to return if the stack is full"""
    def is_full(self):
        if len(self.items) == self.size:
            return True
        else:
            return False
          
"""function to push data into the stack"""
    def push(self, data):
        if not self.is_full():
            self.items.append(data)

""" function to pop elements in the stack from top"""
    def pop(self):
        if not self.is_empty():
            # Write code here
            self.items.pop()

"""to display all the elements in the stack"""         
    def status(self):
        for element in self.items:
            print(element)
          
"""inputting size and query of the stack"""
size, queries = map(int, input().rstrip().split())

"""creating object module"""
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
