"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

import sys
sys.path.append('../singly_linked_list/')
print(sys.path)
from singly_linked_list import LinkedList


# Not allowed to use lists

class Stack:# In a stack, a new element is added at one end and an element is removed from that end only. 
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        
    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)
       

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()
        else:
            return None

    def len(self):
        return self.size
        
    
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size +=1 
#         self.storage.insert(0, value)

#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         self.size -= 1
#         node = self.storage.pop(0)
#         return node
        

